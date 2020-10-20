# Gomoku

Gomoku is a two player five-in-a-row game played on a 15x15 game.

This repository hosts a Gomoku AI based around Victor Allis's Threat Space Search algorithm.

## Repository Structure

This repository is split into 3 folders:

- game
This folder contains all the Gomoku AI and board logic, wrapped up in a python package.

- static
This folder contains front-end code, written using react/react-redux/webpack.

- server
This folder contains a simple flask server that serves our react front-end.

## Quickstart
There are several ways to start this full stack application.
Once started, the app can be located at http://localhost:80.

Invoke + Docker
```console
pip install invoke
inv build run
```

Manually:
```console
pip install ./game
npm run --prefix ./static build
python server/server.py
```
