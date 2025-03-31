import torch
from diffusers import FluxFillPipeline
from diffusers.utils import load_image

from PIL import Image
import io


def generate_text_guided_image_to_image(image, mask, prompt):
    # image = load_image(
    #     "https://huggingface.co/datasets/diffusers/diffusers-images-docs/resolve/main/cup.png")
    # mask = load_image(
    #     "https://huggingface.co/datasets/diffusers/diffusers-images-docs/resolve/main/cup_mask.png")

    pil_image = Image.open(image).convert('RGB')
    pil_mask = Image.open(mask).convert('RGB')

    pipe = FluxFillPipeline.from_pretrained(
        "C:\\Users\\633578\\Repositories\\image-chef\\api\\image_chef_api\\models\\FLUX.1-Fill-dev",
        torch_dtype=torch.float32
    )
    image = pipe(
        prompt=prompt,
        image=pil_image,
        mask_image=pil_mask,
        height=512,
        width=512,
        guidance_scale=30,
        num_inference_steps=2,
        max_sequence_length=512,
        generator=torch.Generator("cpu").manual_seed(0)
    ).images[0]

    image.save("flux-fill-dev.png")
