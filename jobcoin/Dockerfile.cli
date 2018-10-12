FROM ubuntu:18.04

WORKDIR /usr/src/app/

RUN apt-get update -y && apt-get upgrade -y && apt-get install -y \
    vim \
    python3 \
    python3-pip


COPY ./requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . ./

CMD bash
