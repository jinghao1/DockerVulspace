ARG AGENT_FROM=local

FROM python:3.6-bullseye as from_github
RUN git clone https://github.com/HXSecurity/DongTai-agent-python.git /DongTai-agent-python
COPY config.example.json config.json* /DongTai-agent-python/dongtai_agent_python/

FROM python:3.6-bullseye as from_local
COPY config.example.json ./DongTai-agent-python* /DongTai-agent-python/

FROM from_${AGENT_FROM}

ENV PYTHONUNBUFFERED 1
ARG PYPI_MIRROR="https://pypi.org/simple"
ARG DEBIAN_MIRROR=""

WORKDIR /code
ADD ./flasksrc/requirements.txt /code/

RUN if test "x${DEBIAN_MIRROR}" != "x"; then sed -i "s@deb.debian.org@${DEBIAN_MIRROR}@g" /etc/apt/sources.list; fi \
  && if test "x${DEBIAN_MIRROR}" != "x"; then sed -i "s@security.debian.org@${DEBIAN_MIRROR}@g" /etc/apt/sources.list; fi \
  && apt-get update -y \
  && export LC_ALL=C \
  && apt install -y libc6-dev gcc make cmake libpq-dev libldap2-dev libsasl2-dev unzip vim \
  && pip install --upgrade pip -i ${PYPI_MIRROR} \
  && pip install -r requirements.txt -i ${PYPI_MIRROR} \
  && pip install /DongTai-agent-python/ \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
