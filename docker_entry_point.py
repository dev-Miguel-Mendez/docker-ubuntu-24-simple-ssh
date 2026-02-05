

#! This file is for things that we need to make sure are executed at container startup, NOT AT BUILD TIME with "RUN".
#! Also, the only reason why we do it here is because will use the CMD for something else OR CMD could be replaced in the future.

#! This entry file is usually written in bash, but I did it in Python just because I prefer it and Python is installed in the ubuntu image.

import subprocess
import os
import sys

subprocess.run(["/usr/sbin/sshd"], shell=True) #! This starts the SSH server.  Need to execute this manually because there is no SystemD in the container
    #! You need to already have created a "/run/sshd" directory for this to work. Read why in the Dockerfile.


ALLOWED_PUBLIC_KEY = os.environ.get("ALLOWED_PUBLIC_KEY")

if not (ALLOWED_PUBLIC_KEY):
    raise RuntimeError("ALLOWED_PUBLIC_KEY required")


subprocess.run("echo $ALLOWED_PUBLIC_KEY > /root/.ssh/authorized_keys", shell=True)



# try:
#     print(sys.argv[0])  #$ This   will be the  name of this file (docker_entry_point.py)
#     print(sys.argv[1])  #$ This will be the first argument passed by CMD in the Dockerfile.
#     print(sys.argv[2])  #$ This will be the second, and so on.
#     print(sys.argv[1:]) #$ This will be all the arguments passed by CMD in the Dockerfile after the first one.

# finally:
#     pass



#*  What's os.execvp?
    #$ It will replace the current process with the new one. It is like "exec" in Linux.
#*  What does it need?
    #$ First arg: A string with the path to the new program to execute.
    #$ Second arg: A list of arguments to pass to the new program.
 

os.execvp(sys.argv[1], sys.argv[1:])
