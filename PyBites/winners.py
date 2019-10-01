"""
Bite 103. Loop through a dictionary and pluralise a word
You're given a dictionary of people and the number of games they've won.
User a for loop to iterate over the dictionary and print out the users name and how many games they've won
sara has won n games
To make it human readable, pluralise the word game to suit the number of games won.
"""

games_won = dict(sara=0, bob=1, tim=5, julian=3, jim=1)


# noinspection PyDefaultArgument
def print_game_stats(input_dict=games_won):
    """Loop through games_won's dict (key, value) pairs (dict.items)
       printing (print, not return) how many games each person has won,
       pluralize 'game' based on number.

       Expected output (ignore the docstring's indentation):

       sara has won 0 games
       bob has won 1 game
       tim has won 5 games
       julian has won 3 games
       jim has won 1 game

       (Note that as of Python 3.7 - which we're using atm - dict insert order is retained
        so no sorting is required for this Bite.)
    """
    for key, value in input_dict.items():
        if value == 1:
            games = "game"
        else:
            games = "games"
        print(f'{key} has won {value} {games}')
    pass
