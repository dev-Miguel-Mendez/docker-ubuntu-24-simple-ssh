Once the container is running, you can check if SSH is running on port 22 by trying to connect via SSH to your own instance:

`
    docker exec -it <container ID> bash
    ssh localhost -p 22
`