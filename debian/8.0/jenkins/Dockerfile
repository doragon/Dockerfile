FROM jenkins

MAINTAINER koide

USER root
RUN apt-get -y update
RUN apt-get -y install vim curl wget git sudo python-pip
RUN pip install docker-py

USER jenkins
ENV HOME /var/jenkins_home
ENV JENKINS_HOME /var/jenkins_home
ENV JENKINS_VERSION 1.554.1
ENV JENKINS_UC https://updates.jenkins-ci.org

ADD ./workspace /var/

VOLUME /var/jenkins_home

EXPOSE 8080
EXPOSE 50000

ENTRYPOINT ["/usr/local/bin/jenkins.sh"]
