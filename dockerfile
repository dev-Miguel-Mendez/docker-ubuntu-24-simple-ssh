FROM ubuntu:24.04

RUN apt update
RUN apt install openssh-server -y #! "apt-get" is recommended over "apt" for scripting. I will keep it as "apt" for now though.

RUN rm -rf /var/lib/apt/lists/* #$ This just cleans up downloaded files only needed for installation (reduce image size)

RUN mkdir -p /run/sshd #$ This folder is required for the sshd (SSH daemon) for temporary state. Since there is no SystemD in the container (which would create this folder by default) we need to create it manually.


#! Read `entry_pint.sh` for more information.
COPY docker_entry_point.py /docker_entry_point.py
RUN chmod 777 /docker_entry_point.py
#- Whatever process this starts becomes the process with PID of 1 when the container starts:
#- Use ENTRYPOINT when you want to reuse the container or run aditional processes other than the one in CMD.
ENTRYPOINT ["python3", "/docker_entry_point.py"]


EXPOSE 22

#! These will be passed as arguments to the ENTRYPOINT process:
CMD ["sleep", "infinity"] 