FROM unfairbanks/docker-ipython-notebook

MAINTAINER koide

ENV HOME /root

RUN apt-get update && \
    apt-get -y install ansible sshpass openssl curl wget sshpass ipmitool && \
    pip install requests paramiko

VOLUME ['/tmp/notebook']

EXPOSE 22 8080

CMD /run.sh
