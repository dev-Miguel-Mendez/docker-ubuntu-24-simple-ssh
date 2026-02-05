import subprocess




DEFAULT_IMAGE_NAME = "ubuntu-24-simple-ssh"
DEFAULT_CONTAINER_NAME = "container-ubuntu-24-simple-ssh"


image_name = input(f"Enter the image name (default: {DEFAULT_IMAGE_NAME}): ") or DEFAULT_IMAGE_NAME
container_name  = input(f"Enter the container name (default: {DEFAULT_CONTAINER_NAME}): ") or DEFAULT_CONTAINER_NAME

DEFAULT_ALLOWED_PUBLIC_KEY = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINpNvRc7lK2O6yY3kL61HqDjN0o6q/a9q+U1Mw9Fz79"
allowed_public_key = input(f"Enter the allowed public key (default: {DEFAULT_ALLOWED_PUBLIC_KEY}): ") or DEFAULT_ALLOWED_PUBLIC_KEY

subprocess.run(f"docker run --name {container_name} -d {image_name} -e ALLOWED_PUBLIC_KEY={allowed_public_key}", shell=True)