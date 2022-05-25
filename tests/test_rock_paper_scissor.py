from main.rock_paper_scissor import Choice, Result, RockPaperScissor


def test_player_wins():
    assert (
        RockPaperScissor.generate_result(
            player_choice=Choice.ROCK,
            computer_choice=Choice.SCISSOR,
        )
        is Result.PLAYER_WON
    )
    assert (
        RockPaperScissor.generate_result(
            player_choice=Choice.SCISSOR,
            computer_choice=Choice.PAPER,
        )
        is Result.PLAYER_WON
    )
    assert (
        RockPaperScissor.generate_result(
            player_choice=Choice.PAPER,
            computer_choice=Choice.ROCK,
        )
        is Result.PLAYER_WON
    )


def test_computer_wins():
    assert (
        RockPaperScissor.generate_result(
            player_choice=Choice.SCISSOR,
            computer_choice=Choice.ROCK,
        )
        is Result.COMPUTER_WON
    )
    assert (
        RockPaperScissor.generate_result(
            player_choice=Choice.PAPER,
            computer_choice=Choice.SCISSOR,
        )
        is Result.COMPUTER_WON
    )
    assert (
        RockPaperScissor.generate_result(
            player_choice=Choice.ROCK,
            computer_choice=Choice.PAPER,
        )
        is Result.COMPUTER_WON
    )


def test_draw():
    assert (
        RockPaperScissor.generate_result(
            player_choice=Choice.ROCK,
            computer_choice=Choice.ROCK,
        )
        is Result.DRAW
    )
    assert (
        RockPaperScissor.generate_result(
            player_choice=Choice.SCISSOR,
            computer_choice=Choice.SCISSOR,
        )
        is Result.DRAW
    )
    assert (
        RockPaperScissor.generate_result(
            player_choice=Choice.PAPER,
            computer_choice=Choice.PAPER,
        )
        is Result.DRAW
    )
