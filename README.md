# gtw - Guess The Witness
## Guess The Witness Bot
A bot, that let's you gamble on the steem blockchain
User send 0.002 SBD to this bot and guess the witness of the block, where the SBD transfer will be included.
If they guessed it right, they will win 0.021 SBD, which will be send back to the same user immediately.

## Requirements
Python 3.6 with steem-python installed

## Installation
Create create a directory for gtw and a virtual environment for Python
``mkdir gtw&&cd gtw``
``python -m venv env``
Source it
``source env/bin/activate``
Install steem-python
``pip install steem-pyhton``

Clone the repository
``git clone https://github.com/isnochys/gtw.git``

## Usage
``(env)$ python gtw.py``
Make a crontab entry and let this bot run every x minutes to check on the bot steem account.
Or run it by hand for testing.
