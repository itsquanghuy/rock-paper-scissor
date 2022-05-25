from main.engines.game import generate_result
from main.enums.game import Choice, Result


def test_player_wins():
    assert (
        generate_result(
            player_choice=Choice.ROCK,
            computer_choice=Choice.SCISSOR,
        )
        is Result.PLAYER_WON
    )
    assert (
        generate_result(
            player_choice=Choice.SCISSOR,
            computer_choice=Choice.PAPER,
        )
        is Result.PLAYER_WON
    )
    assert (
        generate_result(
            player_choice=Choice.PAPER,
            computer_choice=Choice.ROCK,
        )
        is Result.PLAYER_WON
    )


def test_computer_wins():
    assert (
        generate_result(
            player_choice=Choice.SCISSOR,
            computer_choice=Choice.ROCK,
        )
        is Result.COMPUTER_WON
    )
    assert (
        generate_result(
            player_choice=Choice.PAPER,
            computer_choice=Choice.SCISSOR,
        )
        is Result.COMPUTER_WON
    )
    assert (
        generate_result(
            player_choice=Choice.ROCK,
            computer_choice=Choice.PAPER,
        )
        is Result.COMPUTER_WON
    )


def test_draw():
    assert (
        generate_result(
            player_choice=Choice.ROCK,
            computer_choice=Choice.ROCK,
        )
        is Result.DRAW
    )
    assert (
        generate_result(
            player_choice=Choice.SCISSOR,
            computer_choice=Choice.SCISSOR,
        )
        is Result.DRAW
    )
    assert (
        generate_result(
            player_choice=Choice.PAPER,
            computer_choice=Choice.PAPER,
        )
        is Result.DRAW
    )
