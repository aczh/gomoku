# Introduction

Flask/MongoEngine/SocketIO backend.

## Quickstart

Run the server via:
```console
pip install -r requirements.txt
python server.py
```
Note that the Flask server is dependent on the front-end being built.

The server looks in `../static/build` and `../static/public` for `bundle.js` and `index.html` respectively.

## Structure
- Flask code is found in the `api` directory.
- MongoEngine models are found in the `models` directory.
- SocketIO code is found in `socket_server.py`.
- Everything is initialized in `server.py`.
