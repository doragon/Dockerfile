# OS
 * Ubuntu14.04

# Use image
 * [phusion/baseimage-docker](https://github.com/phusion/baseimage-docker)

# How to use
```shell
sudo docker build -t koide/jenkins:base_ubuntu1404 .
```

```shell
sudo docker run -d \
 -p 22 -p 8080 koide/jenkins:base_ubuntu1404 /sbin/my_init
```

```shell
ssh -i ./id_rsa -p xxxx root@xxx.xxx.xxx.xxx
ssh -i ./id_rsa -p xxxx ubuntu@xxx.xxx.xxx.xxx
```
