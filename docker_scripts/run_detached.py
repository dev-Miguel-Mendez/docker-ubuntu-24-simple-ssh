import subprocess




DEFAULT_IMAGE_NAME = "ubuntu-24-simple-ssh"
DEFAULT_CONTAINER_NAME = "container-ubuntu-24-simple-ssh"


image_name = input(f"Enter the image name (default: {DEFAULT_IMAGE_NAME}): ") or DEFAULT_IMAGE_NAME
container_name  = input(f"Enter the container name (default: {DEFAULT_CONTAINER_NAME}): ") or DEFAULT_CONTAINER_NAME

DEFAULT_ALLOWED_PUBLIC_KEY = "abc123"
allowed_public_key = input(f"Enter the allowed public key (default: {DEFAULT_ALLOWED_PUBLIC_KEY}): ") or DEFAULT_ALLOWED_PUBLIC_KEY

CMD = f"docker run --name {container_name} -d {image_name} -e ALLOWED_PUBLIC_KEY={allowed_public_key}"

print(f"Running: \n  {CMD}")

subprocess.run(CMD, shell=True)
