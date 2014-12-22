FROM sameersbn/gitlab:latest

MAINTAINER koide

ADD ./conf/generate_temporarily_email.rb /home/git/gitlab/config/initializers/generate_temporarily_email.rb

EXPOSE 22 80 443

VOLUME ["/home/git/data"]
VOLUME ["/var/log/gitlab"]

ENTRYPOINT ["/app/init"]
CMD ["app:start"]
