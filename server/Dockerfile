FROM ubuntu:16.04

MAINTANER Allen Zhang "allenczhang@gmail.com"

# install dependencies
RUN apt-get update -y && apt-get install -y python-pip python-dev

# copy files
WORKDIR /app
COPY . /app

# install python dependencies
RUN pip install -r requirements.txt

# run flask server
ENTRYPOINT [ "python" ]
CMD [ "server.py" ]
