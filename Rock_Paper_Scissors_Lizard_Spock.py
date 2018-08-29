# This program will prompt and play out a game of Rock, Paper, Scissors, Lizard, Spock

import random

from enum import Enum

# Convert Move names to numbers
class Option(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    LIZARD = 4
    SPOCK = 5

""" Save our list of rules
Each move has an index which contains a set of moves that it will win against
In rock paper scissors lizard spock, each move can win against two other moves """
RULE_DICTIONARY = {
    Option.ROCK: set([Option.SCISSORS, Option.LIZARD]),
    Option.PAPER: set([Option.ROCK, Option.SPOCK]),
    Option.SCISSORS: set([Option.PAPER, Option.LIZARD]),
    Option.LIZARD: set([Option.PAPER, Option.SPOCK]),
    Option.SPOCK: set([Option.ROCK, Option.SCISSORS]),
}

# Save a dictionary of verbs that describe the relationship between the winner and loser
# ie Lizard eats paper or paper disproves spock
VERB_DICTIONARY = {
    Option.ROCK: {Option.SCISSORS: 'crushes', Option.LIZARD: 'crushes'},
    Option.PAPER: {Option.ROCK: 'covers', Option.SPOCK: 'disproves'},
    Option.SCISSORS: {Option.PAPER: 'cuts', Option.LIZARD: 'decapitates'},
    Option.LIZARD: {Option.PAPER: 'eats', Option.SPOCK: 'poisons'},
    Option.SPOCK: {Option.ROCK: 'vaporizes', Option.SCISSORS: 'smashes'},
}

# We need a way to convert numbers to their represented string
NAME_DICTIONARY = {
    Option.ROCK: 'Rock',
    Option.PAPER: 'Paper',
    Option.SCISSORS: 'Scissors',
    Option.LIZARD: 'Lizard',
    Option.SPOCK: 'Spock',
}

# Define a comparable class that stores the user's choice
class State:

    # Constructor - Builds the State object
    def __init__(self, choice):
        self.choice = choice

    # Defines the equality operator for the State object. ie player1 == player2
    def __eq__(self, other):
        return self.choice == other.choice

    # Defines the inequality operator for the State object. ie player1 != player2
    def __ne__(self, other):
        return not self == other

    # Defines the greater than operator for the State object. ie player1 > player2
    def __gt__(self, other):
        return other.choice in RULE_DICTIONARY[self.choice]

    # Defines the less than operator for the State object. ie player1 < player2
    def __lt__(self, other):
        return (self != other and not self > other)

    # Defines the less than or equal to operator for the State object. ie player1 <= player2
    def __le__(self, other):
        return not (self > other)

    # Defines the greater than or equal to operator for the State object. ie player1 >= player2
    def __ge__(self, other):
        return (self > other or self == other)

    # Defines how the State object is converted to a string.
    def __str__(self):
        return NAME_DICTIONARY[self.choice]

    # Describes how one state beats another. ie 'scissors cuts paper'
    def beats(self, other):
        try:
            return self.__str__().capitalize() + ' ' + VERB_DICTIONARY[self.choice][
                other.choice] + ' ' + other.__str__()
        except:
            return False


def main():
    #Change the range for how many rounds will play out for both players
    for i in range(3):
        # Pick a random number, 1-5, for each player
        p1 = State(Option(random.randint(1, 5)))
        p2 = State(Option(random.randint(1, 5)))

        # Print each player's choices
        print('Player 1 chose ' + p1.__str__())
        print('Player 2 chose ' + p2.__str__())

        # Check who won
        if p1 > p2:
            print(p1.beats(p2) + ' -- Player 1 wins!')
        elif p1 == p2:
            print('TIE!!!')
        else:
            print(p2.beats(p1) + ' -- Player 2 wins!')

        # Print an empty line so we don't go insane
        print()


main()