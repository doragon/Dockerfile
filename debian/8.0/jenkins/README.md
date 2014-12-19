# Description
This is useful for using a private docker hub.

# OS
 * Debian8.0

# Use image
 * [cloudbees/jenkins-ci.org-docker](https://github.com/cloudbees/jenkins-ci.org-docker)
 * from [docker-library/java](https://github.com/docker-library/java/tree/2408508f3b000bf997febbdb90a861185a64a260)
 * from debian:jessie 

# How to use
```shell
mkdir jenkins_home
chmod 777 jenkins_home
```

```shell
vim workspace/dockerclient.py
base_url = 'tcp://[DOCKER_SERVER]:4243'
```

```shell
sudo docker build -t koide/jenkins .

sudo docker run -p 28080:8080 -d \
 -v /[PATH]/jenkins/jenkins_home:/var/jenkins_home \
 -v /[PATH]/jenkins/workspace:/var/workspace \
 koide/jenkins
```
