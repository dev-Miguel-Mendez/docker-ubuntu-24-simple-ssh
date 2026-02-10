

#! This file is for things that we need to make sure are executed at container startup, NOT AT BUILD TIME with "RUN".
#! Also, the only reason why we do it here is because will use the CMD for something else OR CMD could be replaced in the future.

#! This entry file is usually written in bash, but I did it in Python just because I prefer it and Python is installed in the ubuntu image.

import subprocess
import os
import sys





result = subprocess.run("/usr/sbin/sshd", shell=True) #! This starts the SSH server.  Need to execute this manually because there is no SystemD in the container
    #! You need to already have created a "/run/sshd" directory for this to work. Read why in the Dockerfile.

if (result.returncode != 0):  raise RuntimeError("Failed to start SSH server")



ALLOWED_PUBLIC_KEY = os.environ.get("ALLOWED_PUBLIC_KEY")

if not (ALLOWED_PUBLIC_KEY):
    raise RuntimeError("ALLOWED_PUBLIC_KEY required")


subprocess.run("mkdir /root/.ssh", shell=True)

with open("/root/.ssh/authorized_keys", "w") as f:
    f.write(ALLOWED_PUBLIC_KEY)



# print(sys.argv[0])  #$ This will be the name of THIS entrypoint file (docker_entry_point.py)
# print(sys.argv[1])  #$ This will be the first argument passed by CMD in the Dockerfile.
# print(sys.argv[2])  #$ This will be the second, and so on.
# print(sys.argv[1:]) #$ This will be all the arguments passed by CMD in the Dockerfile (all items in the argv list from index 1 INCLUDING INDEX 1)



#*  What's os.execvp?

    #! READ either:
        #! Notion page
        #! /home/miguel/Desktop/vsCodeMain/Practice/Python/12-selected-python-topics-single-git-repo

    #$ It will replace the current process with the new one. It uses the "exec" of Linux.

    #$ "v" and "p" are like flags. You need to read what I gave you.

#*  What does "execvp" do IN THIS CASE?
    #$ p: will find the first argument (string) in the $PATH and execute it.

    #$ Second arg: A list of arguments to pass to the new program (YOU ALSO NEED TO INCLUDE).
 


os.execvp(sys.argv[1], sys.argv[1:])
#* So will look like:

# os.execvp("python3", ["python3", "app.py", ...]) #$ Yes, with Python3 REPEATED. That is how `os.execvp` works
