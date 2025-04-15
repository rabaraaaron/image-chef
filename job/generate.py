import torch
from diffusers import FluxPipeline
from azure.storage.blob import BlobServiceClient, BlobClient

import os

from transformers.utils import move_cache
move_cache()


def generate_text_to_image():
    prompt = os.environ.get("PROMPT")
    print(f"PROMPT: {prompt}")
    torch.cuda.empty_cache()

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"DEVICE: {device}")
    print(os.environ.get("FLUX_SCHNELL"))

    pipe = FluxPipeline.from_pretrained(
        os.environ.get("FLUX_SCHNELL"),
        torch_dtype=torch.float32
    )

    # Change inference step for more refinement
    image = pipe(
        prompt,
        guidance_scale=0.0,
        height=512,
        width=512,
        num_inference_steps=2,
        max_sequence_length=256,
        generator=torch.Generator(device="cpu").manual_seed(0)
    ).images[0]
    image.save("flux-schnell.png")


connect_str = os.environ.get("BLOB_CONNECTION_STRING")
blob_service_client = BlobServiceClient.from_connection_string(connect_str)


def upload_image():
    generate_text_to_image()

    # Create a blob client
    blob_client = blob_service_client.get_blob_client(
        container=os.environ.get("CONTAINER_NAME"),
        blob="flux-schnell.png")

    # Upload the file
    local_file_path = "./flux-schnell.png"
    with open(local_file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)


upload_image()
