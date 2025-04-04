import torch
from diffusers import FluxFillPipeline

from PIL import Image
from api.image_chef_api.utils.environment import Environment

config = Environment().config


def generate_text_guided_image_inpainting(image, mask, prompt):
    pil_image = Image.open(image).convert('RGB')
    pil_mask = Image.open(mask).convert('RGB')

    pipe = FluxFillPipeline.from_pretrained(
        config.get("FLUX_FILL"),
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
