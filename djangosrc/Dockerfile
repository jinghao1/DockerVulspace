FROM python:3.6-bullseye
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD ./requirements.txt /code/
#COPY config.json /code/dongtai_agent_python/
RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN sed -i "s@deb.debian.org@mirrors.aliyun.com@g" /etc/apt/sources.list \
    && sed -i "s@security.debian.org@mirrors.aliyun.com@g" /etc/apt/sources.list
RUN   apt-get update -y \
    && export LC_ALL=C \
    && apt install -y  libc6-dev libpq-dev unzip vim
#ADD . /code/