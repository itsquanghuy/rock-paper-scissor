from random import choice as random_pick

from .engines.game import generate_result
from .enums.game import Choice, Result


def _ask_for_player_choice() -> Choice:
    while True:
        player_choice = input("Rock(r), Paper(p), Scissor(s): ")
        if player_choice == "r":
            return Choice.ROCK
        elif player_choice == "p":
            return Choice.PAPER
        elif player_choice == "s":
            return Choice.SCISSOR
        else:
            print("Invalid Choice.")
            continue


def _pick_random_choice():
    return random_pick(Choice.get_list())


def _print_result(
    player_choice: Choice,
    computer_choice: Choice,
) -> None:
    result = generate_result(player_choice, computer_choice)

    if result is Result.PLAYER_WON:
        print("Player won.")
    elif result is Result.COMPUTER_WON:
        print("Computer won.")
    else:
        print("Draw.")


def start_game():
    try:
        while True:
            computer_choice = _pick_random_choice()
            player_choice = _ask_for_player_choice()

            _print_result(player_choice, computer_choice)
    except KeyboardInterrupt:
        print("\nBye!")
        exit()
