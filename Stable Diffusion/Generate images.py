# make sure you're logged in with `huggingface-cli login`, use ldm environment
from torch import autocast
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    use_auth_token="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"
).to("cuda")

prompt = "a photo of an astronaut riding a horse on mars"
with autocast("cuda"):
    image = pipe(prompt)["sample"][0]

image.save("astronaut_rides_horse.png")
