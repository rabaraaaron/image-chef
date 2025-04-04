import torch
from diffusers import StableDiffusionXLImg2ImgPipeline

from PIL import Image
from api.image_chef_api.utils.environment import Environment

config = Environment().config


def generate_image_to_image(image, prompt):
    pil_image = Image.open(image).convert('RGB')

    pipe = StableDiffusionXLImg2ImgPipeline.from_pretrained(
        config.get("FLUX_REFINEMENT"),
        torch_dtype=torch.float32,
        use_safetensors=True,
        variant="fp16"
    )
    pipe.to("cuda")

    image = pipe(prompt, image=pil_image).images[0]

    image.save("flux-refinement.png")
