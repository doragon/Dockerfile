FROM ubuntu:13.10
 
MAINTAINER koide
 
# vim, ifconfig, curl
RUN apt-get -y update
RUN apt-get -y install vim net-tools curl
 
# apache, wsgi
RUN apt-get -y install apache2 libapache2-mod-wsgi
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
 
# conf
ADD ./default.conf /etc/apache2/sites-available/default.conf
RUN ln -s /etc/apache2/sites-available/default.conf /etc/apache2/sites-enabled/default.conf
RUN rm /etc/apache2/sites-enabled/000-default.conf; service apache2 start; a2enmod wsgi; service apache2 stop
