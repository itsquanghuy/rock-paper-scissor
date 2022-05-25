from random import choice as random_pick

from .rock_paper_scissor import Choice, Result, RockPaperScissor


def start_game():
    try:
        while True:
            computer_choice = random_pick(Choice.get_list())
            player_choice = input("Rock(r), Paper(p), Scissor(s): ")
            if player_choice == "r":
                player_choice = Choice.ROCK
            elif player_choice == "p":
                player_choice = Choice.PAPER
            elif player_choice == "s":
                player_choice = Choice.SCISSOR
            else:
                print("Invalid Choice.")
                continue

            result = RockPaperScissor.generate_result(
                player_choice=player_choice,
                computer_choice=computer_choice,
            )

            if result is Result.PLAYER_WON:
                print("Player won.")
            elif result is Result.COMPUTER_WON:
                print("Computer won.")
            else:
                print("Draw.")
    except KeyboardInterrupt:
        print("\nBye!")
        exit()
