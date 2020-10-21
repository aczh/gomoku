# Gomoku

Gomoku is a two player five-in-a-row game played on a 15x15 game.

This repository hosts a Gomoku AI based on Victor Allis's Threat Space Search algorithm.
The AI + game logic is written in Python.
The frontend code is written in react/react-redux/webpack.
The frontend code is deployed using Flask.
The whole project is hosted on AWS: https://ec2-18-208-169-230.compute-1.amazonaws.com/

## Repository Structure

This repository is split into 3 folders:

- game

    This folder contains all the Gomoku AI and board logic, wrapped up in a python package.

- static

    This folder contains front-end code.

- server

    This folder contains a simple flask server that serves the react front-end.

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

## TODO
- Fully implement database.
- Clear notification when a player wins
- Allow move takebacks.
- Users
    - User login
    - Allow users to see their past games
- Gomoku AI
    - Opening book for player 1
    - Deal with memory leaks with cached threat searches
    - Save winning positions
    - Allow game to be played on boards different from 15x15
