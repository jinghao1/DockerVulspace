FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
#COPY config.json /code/dongtai_agent_python/
RUN pip install -r requirements.txt
RUN   apt-get update -y \
    && export LC_ALL=C \
    && apt install -y  libc6-dev unzip vim
#ADD . /code/