from .base import BaseEnum


class Choice(BaseEnum):
    ROCK = 0
    PAPER = 1
    SCISSOR = 2


class Result(BaseEnum):
    DRAW = 0
    PLAYER_WON = 1
    COMPUTER_WON = 2
