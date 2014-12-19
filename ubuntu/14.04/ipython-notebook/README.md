# Description
IPython Notebook + Ansible + etc tools

# OS
 * ubuntu:latest(14.04)

# Use image
 * [docker pull unfairbanks/docker-ipython-notebook](https://registry.hub.docker.com/u/unfairbanks/docker-ipython-notebook/dockerfile/)

# How to use
```shell
sudo docker build -t koide/ipython-notebook .
sudo docker run -d -p 22 -p 18080:8080 \
 --env HONE=/root \
 -v /[PATH]/ipython-notebook/ipython-notebook:/tmp/notebook \
 koide/ipython-notebook
```
