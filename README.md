# Rock Paper Scissor Console Game
[![Build Status](https://app.travis-ci.com/vuhuycto/rock-paper-scissor.svg?branch=main)](https://app.travis-ci.com/vuhuycto/rock-paper-scissor)

## Installation and Setup

### Setup code base

Install [Python 3.7](https://www.python.org/downloads/release/python-376/) and [pip](https://pypi.python.org/pypi/pip) and clone this project:

    $ mkdir ~/rock-paper-scissor
    $ cd ~/rock-paper-scissor
    $ git clone git@github.com:vuhuycto/rock-paper-scissor.git

Set up [Virtualenv](https://virtualenv.pypa.io/en/stable/):

    $ pip install virtualenv
    $ cd ~/
    $ virtualenv env
    $ source ~/env/bin/activate

Install project dependencies:

    $ pip install -r requirements/dev.txt

## Start the game

    $ python run.py

## Testing

Run the tests:

    $ run_tests.cmd
