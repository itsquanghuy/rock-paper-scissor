from .enums import BaseEnum


class Choice(BaseEnum):
    ROCK = 0
    PAPER = 1
    SCISSOR = 2


class Result(BaseEnum):
    DRAW = 0
    PLAYER_WON = 1
    COMPUTER_WON = 2


class RockPaperScissor:
    @staticmethod
    def generate_result(
        player_choice: Choice,
        computer_choice: Choice,
    ) -> Result:
        if (player_choice.value + 1) % 3 == computer_choice.value:
            return Result.COMPUTER_WON
        elif player_choice.value == computer_choice.value:
            return Result.DRAW
        else:
            return Result.PLAYER_WON
