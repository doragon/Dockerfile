FROM ubuntu:13.10
 
MAINTAINER koide
 
# ssh:root
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update && apt-get clean
 
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo "root:root" |chpasswd
 
# ssh:user
RUN apt-get install -y sudo
RUN useradd --create-home -s /bin/bash doragon
RUN adduser doragon sudo
RUN echo "doragon:pass" | chpasswd
RUN mkdir /home/doragon/.ssh/
 
RUN echo >> /etc/sudoers
RUN echo "doragon ALL=(ALL) ALL" >> /etc/sudoers
 
EXPOSE 22
CMD /usr/sbin/sshd -D
