FROM ubuntu:13.10
 
MAINTAINER koide
 
RUN apt-get -y update
RUN apt-get -y install curl net-tools unzip wget
 
# conul
RUN wget -O /tmp/0.2.0_linux_amd64.zip https://dl.bintray.com/mitchellh/consul/0.2.0_linux_amd64.zip
RUN unzip /tmp/0.2.0_linux_amd64.zip
RUN chmod 750 ./consul
RUN mv ./consul /usr/bin/
RUN mkdir /opt/consul/
RUN rm /tmp/0.2.0_linux_amd64.zip
 
EXPOSE 8300 8301 8302 8400 8500 8600
 
CMD ["/bin/bash"]
