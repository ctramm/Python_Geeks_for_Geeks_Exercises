"""
Bite 102. Infinite loop, input, continue and break
In this Bite we'll get you to take user input and see if it matches items within a list.
In the while loop ask the user to enter a color and capture that input.
Check to see whether they've entered "quit", if so, print bye and exit the loop.
If not, check to see whether the color is in the VALID_COLORS list.
If it is, print lower case. If not, print Not Valid Color and continue the loop.
As you want to ask the user over and over again til they quit, you can use an infinite while loop.
"""
VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
    while True:
        color = input("Enter a color or quit").lower()
        if color == "quit":
            print('bye')
            break
        elif color not in VALID_COLORS:
            print("Not a valid color")
            continue
        else:
            print(f"{color}")
