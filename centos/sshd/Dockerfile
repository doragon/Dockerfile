FROM centos:6.4
 
MAINTAINER doragon
 
# Install sshd
RUN yum -y install openssh-server openssh-clients
 
# Configure sshd
RUN /usr/bin/ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key -C '' -N ''
RUN /usr/bin/ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -C '' -N ''
 
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config
 
RUN yum -y install passwd sudo
RUN adduser USER
RUN echo PASSWORD | passwd USER --stdin
RUN mkdir /home/USER/.ssh/
 
RUN echo >> /etc/sudoers
RUN echo "USER    ALL=(ALL)       ALL" >> /etc/sudoers
 
RUN touch /etc/sysconfig/network
 
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
