from main.enums.game import Choice, Result


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
