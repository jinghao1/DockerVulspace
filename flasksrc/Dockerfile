FROM python:3.6-bullseye

ENV PYTHONUNBUFFERED 1
ARG PYPI_MIRROR="https://pypi.org/simple"
ARG DEBIAN_MIRROR=""
ARG DEBIAN_SECURITY_MIRROR=""

WORKDIR /code
ADD ./requirements.txt /code/

RUN pip install --upgrade pip -i ${PYPI_MIRROR} \
  && pip install -r requirements.txt -i ${PYPI_MIRROR} \
  && if test "x${DEBIAN_MIRROR}" != "x"; then sed -i "s@deb.debian.org@${DEBIAN_MIRROR}@g" /etc/apt/sources.list; fi \
  && if test "x${DEBIAN_SECURITY_MIRROR}" != "x"; then sed -i "s@security.debian.org@${DEBIAN_SECURITY_MIRROR}@g" /etc/apt/sources.list; fi

RUN apt-get update -y \
  && export LC_ALL=C \
  && apt install -y  libc6-dev libpq-dev unzip vim
