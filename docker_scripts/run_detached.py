import subprocess




DEFAULT_IMAGE_NAME = "ubuntu-24-simple-ssh"
DEFAULT_CONTAINER_NAME = "container-ubuntu-24-simple-ssh"


image_name = input(f"Enter the image name (default: {DEFAULT_IMAGE_NAME}): ") or DEFAULT_IMAGE_NAME
container_name  = input(f"Enter the container name (default: {DEFAULT_CONTAINER_NAME}): ") or DEFAULT_CONTAINER_NAME

subprocess.run(f"docker run --name {container_name} -d --rm {image_name}", shell=True)