FROM ubuntu:13.10

MAINTAINER doragon

RUN apt-get update && apt-get clean
RUN apt-get install -y git-core curl gcc build-essential libssl-dev
RUN apt-get install -y vim tree openssh-server sudo

# ssh:root
RUN mkdir /var/run/sshd
RUN echo "root:root" |chpasswd

# ssh:user
RUN useradd --create-home -s /bin/bash doragon
RUN adduser doragon sudo
RUN echo "doragon:doragon" | chpasswd
RUN mkdir /home/doragon/.ssh/

RUN echo >> /etc/sudoers
RUN echo "doragon ALL=(ALL) ALL" >> /etc/sudoers

# golang
RUN curl -OL http://golang.org/dl/go1.3.linux-amd64.tar.gz
RUN tar zxvf go1.3.linux-amd64.tar.gz -C /usr/local
RUN mkdir /root/gocode
RUN mkdir /root/gocode/bin /root/gocode/src /root/gocode/pkg

# saucy sshd
RUN sed -i 's/.*session.*required.*pam_loginuid.so.*/session optional pam_loginuid.so/g' /etc/pam.d/sshd

# .vimrc
RUN git clone https://github.com/doragon/others.git /root/others
RUN cp /root/others/.vimrc /root/.vimrc
RUN rm -rf /root/others

EXPOSE 22
CMD /usr/sbin/sshd -D
