# OS
 * CentOS6

# Version(2014/11/06)
 * elasticsearch: 1.3.5
 * JVM: 1.7.0_71
 * nginx: 1.6.2
 * td-agent: 0.10.55
 * fluentd: 0.10.55
 * kibana: 3.1.1

# Fluentd Plugins
 * /usr/lib64/fluent/ruby/bin/fluent-gem install fluent-plugin-elasticsearch
 * /usr/lib64/fluent/ruby/bin/fluent-gem install fluent-plugin-typecast
 * /usr/lib64/fluent/ruby/bin/fluent-gem install fluent-plugin-map
 * /usr/lib64/fluent/ruby/bin/fluent-gem install fluent-plugin-geoip
 * /usr/lib64/fluent/ruby/bin/fluent-gem install fluent-plugin-rewrite-tag-filter

# Elasticsearch Plugins
 * /usr/share/elasticsearch/bin/plugin -install mobz/elasticsearch-head
 * /usr/share/elasticsearch/bin/plugin -install lmenezes/elasticsearch-kopf
 * /usr/share/elasticsearch/bin/plugin -install elasticsearch/marvel/latest
 * /usr/share/elasticsearch/bin/plugin -install royrusso/elasticsearch-HQ
 * /usr/share/elasticsearch/bin/plugin -install elasticsearch/elasticsearch-analysis-kuromoji/2.3.0

# Links of Elasticsearch Plugins
 * http://xxx.xxx.xxx.xxx:9200/_plugin/head
 * http://xxx.xxx.xxx.xxx:9200/_plugin/kopf
 * http://xxx.xxx.xxx.xxx:9200/_plugin/marvel
 * http://xxx.xxx.xxx.xxx:9200/_plugin/HQ

# How to use
```shell
sudo docker build -t koide/efk:centos6 .
```

```shell
sudo docker run -d \
 -p 9200:9200 -p 9300:9300 -p 24220:24220 -p 24224:24224 -p 8080:80 \
 -e "ES_HEAP_SIZE=200m" -e "NODE_NAME=es1" \
 koide/efk:centos6
```
