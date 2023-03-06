FROM registry.cn-hangzhou.aliyuncs.com/pazhoulab/brain_gate:0.1
COPY . /workspace
WORKDIR /workspace
RUN apt-get update \ 
    && apt-get install -y python3.10 python3-pip vim curl  git redis-server mysql-client-core-8.0 net-tools \
    && pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple/ \
    && go env -w GOPROXY=https://goproxy.cn,direct \
    &&  go build . 

EXPOSE 7777
CMD ["/bin/bash", "-c", "sh run.sh"]