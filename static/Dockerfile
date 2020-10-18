FROM node:latest

MAINTAINER Allen Zhang "allenczhang@gmail.com"

WORKDIR /app
COPY . /app

# install dependencies
RUN npm install

EXPOSE 8080

CMD [ "npm", "start" ]
