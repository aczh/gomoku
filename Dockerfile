FROM node:latest as static-build
WORKDIR /app/static
COPY ./static .
RUN npm install
ARG ENV
RUN if [ "$ENV" = "development" ]; then npm run build ; else npm run prod ; fi

FROM python:3.7-slim-buster

# install dependencies
RUN apt-get update -y
RUN apt-get install -y python-pip python3-dev
RUN apt-get install -y libgmp3-dev libmpc-dev libmpfr-dev

# install gomoku
WORKDIR /app/game
COPY ./game .
RUN pip3 install .

# copy files
WORKDIR /app/server
COPY ./server .
COPY --from=static-build /app/static/build /app/static/build
COPY --from=static-build /app/static/public /app/static/public

# install python dependencies
RUN pip3 install -r requirements.txt

# run flask server
EXPOSE 80
ENTRYPOINT [ "python3" ]
CMD [ "server.py" ]
