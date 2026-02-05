import subprocess




default_image_name = "ubuntu-24-simple-ssh"
default_container_name = "container-ubuntu-24-simple-ssh"


container_name  = input(f"Enter the container name (default: {default_container_name}): ") or default_container_name
image_name = input(f"Enter the image name (default: {default_image_name}): ") or default_image_name




subprocess.run(f"docker run --name {container_name} -d --rm {image_name}", shell=True)