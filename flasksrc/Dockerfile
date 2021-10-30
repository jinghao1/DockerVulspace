
FROM python:3.6.6
RUN mkdir /code
WORKDIR /code
ADD ./flasksrc /code
WORKDIR /code
RUN pip install -r requirement.txt
RUN   apt-get update -y \
    && export LC_ALL=C \
    && apt install -y  libc6-dev unzip vim
CMD ["python", "app.py"]