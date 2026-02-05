#!/bin/bash


#! This file is for things that we need to make sure are executed at container startup, NOT AT BUILD TIME with "RUN".
#! Also, the only reason why we do it here is because will use the CMD for something else OR CMD could be replaced in the future.


/usr/sbin/sshd #! This starts the SSH server.  Need to execute this manually because there is no SystemD in the container
     #! You need to already have created a "/run/sshd" directory for this to work. Read why in the Dockerfile.

echo "Started!"

exec "$@" #! This executes the command passed as CMD in the Dockerfile.