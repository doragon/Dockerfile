#!/bin/bash
 
### 1.Redis ###
# docker run --name gitlab-redis -d \
#  sameersbn/redis:latest
 
### 2.MySQL ###
# docker run --name gitlab-mysql -d \
#  -e 'DB_NAME=gitlabhq_production' \
#  -e 'DB_USER=gitlab' \
#  -e 'DB_PASS=password' \
#  -v /mnt/workspace/gitlab/mysql:/var/lib/mysql \
#  sameersbn/mysql:latest
 
### 3.1.GitLab ###
# docker run -d -p 10022:22 -p 10080:80 \
#  -e "GITLAB_HOST=localhost" \
#  -v /mnt/workspace/gitlab/git:/home/git/data \
#  --link gitlab-mysql:mysql \
#  --link gitlab-redis:redisio \
#  sameersbn/gitlab:latest

### 3.2.GitLab(ldap) ###
# docker build -t koide/gitlab:latest .
# 
# docker run -d -p 10022:22 -p 10080:80 \
#  --env-file ./conf/env \
#  -v /mnt/workspace/gitlab/git:/home/git/data \
#  -v /mnt/workspace/gitlab/log:/var/log/gitlab \
#  --link gitlab-mysql:mysql \
#  --link gitlab-redis:redisio \
#  koide/gitlab:latest
