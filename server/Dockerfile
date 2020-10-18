FROM ubuntu:16.04

MAINTAINER Allen Zhang "allenczhang@gmail.com"

# install dependencies
RUN apt-get update -y
RUN apt-get install -y python-pip python3-dev
RUN apt-get install -y libgmp3-dev libmpc-dev libmpfr-dev

# copy files
WORKDIR /app
COPY . /app

# install python dependencies
RUN pip install -r requirements.txt

# run flask server
ENTRYPOINT [ "python" ]
CMD [ "server.py" ]
