#!/bin/bash

# elasticsearch start
/usr/share/elasticsearch/bin/elasticsearch -d

# kibana start
/usr/sbin/nginx -c /etc/nginx/nginx.conf

# td-agent start
service td-agent start