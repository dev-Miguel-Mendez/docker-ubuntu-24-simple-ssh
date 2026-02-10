FROM ubuntu:24.04






#! We need to run everything in a single RUN so that the downloads from `apt update` are not cached in a layer and can be deleted in the same layer where they are downloaded.
RUN apt update \ 
    && apt install -y --no-install-recommends openssh-server python3\  
    && rm -fr /var/lib/apt/lists/* #$ This removes the package index files from `apt update`
#! "apt-get" is recommended over "apt" for scripting. I will keep it as "apt" for now though.
#- "--no-install-recommends" reduced 200MB!!!
#- rm -fr /var/lib/apt/lists/*  reduced 100MB!!!


RUN mkdir -p /run/sshd #$ This folder is required for the sshd (SSH daemon) for temporary state. Since there is no SystemD in the container (which would create this folder by default) we need to create it manually.


#! Read `entry_pint.sh` for more information.
COPY src/docker_entry_point.py /docker_entry_point.py
RUN chmod 777 /docker_entry_point.py
#- Whatever process this starts becomes the process with PID of 1 when the container starts:
#- Use ENTRYPOINT when you want to reuse the container or run aditional processes other than the one in CMD.
ENTRYPOINT ["python3", "/docker_entry_point.py"]


EXPOSE 22

#$ Just for testing
COPY src/test_python_program.py /test_python_program.py 
RUN chmod 777 /test_python_program.py


#! These will be passed as arguments to the ENTRYPOINT process:
CMD ["python3", "-u", "/test_python_program.py"] 
#! "-u" is for Python to no buffer it's output which does by default.

