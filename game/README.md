# Introduction

Gomoku game + AI implementation.

## Tests
```python
pip install .
pytest
```

## Play

```python
python3 main.py
```
main.py can be modified to create a game with different players/levels of AI.

## Structure
Bitboard implementation can be found in `board.py`.
Game logic can be found in `game.py`.
Threat detection and an implementation of Threat Space Search can be found in the `threat` folder.
Player implementations can be found in the `player` folder.
