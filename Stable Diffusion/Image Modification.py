import os

path_to_image = ""
text = ""
terminal_command = "python stable-diffusion/scripts/img2img.py --prompt " + text + " --init-img " + path_to_image + " --strength 0.8"
os.system(terminal_command)
