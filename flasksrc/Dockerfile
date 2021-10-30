
FROM python:3.6.6
RUN mkdir /code

ADD requirements.txt /code/

WORKDIR /code
RUN pip install -r requirements.txt
RUN   apt-get update -y \
    && export LC_ALL=C \
    && apt install -y  libc6-dev unzip vim
