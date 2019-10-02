"""
Bite 103. Loop through a dictionary and pluralise a word
You're given a dictionary of people and the number of games they've won.
User a for loop to iterate over the dictionary and print out the users name and how many games they've won
sara has won n games
To make it human readable, pluralise the word game to suit the number of games won.
"""

games_won = dict(sara=0, bob=1, tim=5, julian=3, jim=1)


# noinspection PyDefaultArgument,PyShadowingNames
def print_game_stats(games_won=games_won):
    for name, num_games in games_won.items():
        games = "game" if num_games == 1 else "games"
        print(f'{name} has won {num_games} {games}')
