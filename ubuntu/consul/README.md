# environment
* ubuntu14.04
* docker0.11

# memo
* ubuntu13.10
* consul

# command
docker build -t consul .
docker run --net=host -it consul
