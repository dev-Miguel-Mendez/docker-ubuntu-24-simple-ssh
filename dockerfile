FROM ubuntu:24.04

RUN apt update
RUN apt install openssh-server -y #! "apt-get" is recommended over "apt" for scripting. I will keep it as "apt" for now though.

RUN rm -rf /var/lib/apt/lists/* #$ This just cleans up downloaded files only needed for installation (reduce image size)

RUN mkdir -p /run/sshd #$ This folder is required for the sshd (SSH daemon) for temporary state. Since there is no SystemD in the container (which would create this folder by default) we need to create it manually.


#! Read `entry_pint.sh` for more information.
COPY docker_entry_point.sh /docker_entry_point.sh
RUN chmod 777 /docker_entry_point.sh
ENTRYPOINT ["/docker_entry_point.sh"]




EXPOSE 22

CMD ["sleep", "infinity"]