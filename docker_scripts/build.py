import subprocess


DEFAULT_IMAGE_NAME = "priapisman677/ubuntu-24-simple-ssh"

image_name = input(f"Enter the image name (default: {DEFAULT_IMAGE_NAME}): ") or DEFAULT_IMAGE_NAME

subprocess.run(f"docker build -t {image_name} .", shell=True)