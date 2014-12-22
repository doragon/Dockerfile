# How to use
## Preparation
``` shell
mkdir git
mkdir log
mkdir mysql
chmod 777 git
chmod 777 log
chmod 777 mysql
```

## Run Redis Container
``` shell
docker run --name gitlab-redis -d \
 sameersbn/redis:latest
```

## Run MySQL Container
``` shell
docker run --name gitlab-mysql -d \
 -e 'DB_NAME=gitlabhq_production' \
 -e 'DB_USER=gitlab' \
 -e 'DB_PASS=password' \
 -v /[PATH]/gitlab/mysql:/var/lib/mysql \
 sameersbn/mysql:latest
```

## Run GitLab Container
### Create new_password
```shell
docker run -it sameersbn/gitlab:latest slappasswd -s new_password
```

### Usually
Modify localhost to your host.

``` shell
docker run -d -p 10022:22 -p 10080:80 \
 -e "GITLAB_HOST=localhost" \
 -v /[PATH]/gitlab/git:/home/git/data \
 -v /[PATH]/gitlab/log:/var/log/gitlab \
 --link gitlab-mysql:mysql \
 --link gitlab-redis:redisio \
 sameersbn/gitlab:latest
```

### If you use LDAP
Modify localhost to your host and LDAP options in env file.

``` shell
docker build -t koide/gitlab:latest .

docker run -d -p 10022:22 -p 10080:80 \
 --env-file ./code/conf/env \
 -v /[PATH]/gitlab/git:/home/git/data \
 -v /[PATH]/gitlab/log:/var/log/gitlab \
 --link gitlab-mysql:mysql \
 --link gitlab-redis:redisio \
 koide/gitlab:latest
```

# Links
 * [LDAP server in CentOS 6.x](http://dan-project.blog.so-net.ne.jp/2013-03-29)
 * [Set up GitLab(Authentication LDAP)](http://www.ramuda.co.jp/techlabo/archives/864)
 * [sameersbn/docker-gitlab](https://github.com/sameersbn/docker-gitlab)
 * [Using LDAP server for authentication backend](https://fumiyas.github.io/gitlab/install-omnibus.html)
