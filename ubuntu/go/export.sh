GOROOT=/usr/local/go
GOPATH=$HOME/gocode
PATH=$PATH:$GOROOT/bin:$GOPATH/bin
RUN curl -o /usr/local/src/export.sh https://raw.githubusercontent.com/doragon/Dockerfile/master/ubuntu/go/export.sh
