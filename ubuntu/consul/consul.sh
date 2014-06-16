#!/bin/sh
 
# consul server
cd /root
IP=`ifconfig eth1|grep inet|awk '{print $2}'|cut -d: -f2`
consul agent -server -bootstrap -client=$IP -dc=local -node=consul1 -data-dir=/tmp/consul  -bind=$IP >> consul.log 2>&1 &

