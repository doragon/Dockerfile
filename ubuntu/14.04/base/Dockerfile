FROM phusion/baseimage:0.9.15

MAINTAINER koide

RUN apt-get -y update

ENV HOME /root
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

# Setting root
ADD ./id_rsa.pub /tmp/your_key
RUN cat /tmp/your_key >> /root/.ssh/authorized_keys && \
    chmod 600 /root/.ssh/authorized_keys

# Add user
ENV USERNAME ubuntu
RUN adduser --disabled-password --gecos '' ${USERNAME}
RUN mkdir -m 700 /home/${USERNAME}/.ssh && \
    chown ${USERNAME}:${USERNAME} /home/${USERNAME}/.ssh
RUN cat /tmp/your_key >> /home/${USERNAME}/.ssh/authorized_keys && \
    chmod 600 /home/${USERNAME}/.ssh/authorized_keys && \
    rm -f /tmp/your_key
RUN echo '${USERNAME} ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \
    echo '${USERNAME}:${USERNAME}' | chpasswd
RUN chown -R ${USERNAME}:${USERNAME} /home/${USERNAME}/

CMD ['/sbin/my_init']
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
