import subprocess


default_image_name = "ubuntu-24-simple-ssh"

image_name = input(f"Enter the image name (default: {default_image_name}): ") or default_image_name

subprocess.run(f"docker build -t {image_name} .", shell=True)