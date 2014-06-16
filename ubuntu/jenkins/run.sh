#!/bin/bash
 
docker build -t doragon/jenkins .
docker run -d -p 2223:22 -p 8081:8080 -v /root/python/test:/data/test doragon/jenkins
