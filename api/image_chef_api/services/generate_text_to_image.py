import torch
from diffusers import FluxPipeline


def generate_text_to_image(prompt: str):
    print(f"PROMPT: {prompt}")
    torch.cuda.empty_cache()

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"DEVICE: {device}")

    pipe = FluxPipeline.from_pretrained(
        "C:\\Users\\633578\\Repositories\\image-chef\\api\\image_chef_api\\models\\FLUX.1-schnell",
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
