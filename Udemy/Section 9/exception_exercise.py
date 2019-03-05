"""
Section 9: Exception Handling Exercise

Create a dictionary "car"
Create 3 keys: make, model, year

Try to access the color key. Remember, we never created the color key, so it's going to throw an exception.
    You need to handle the exception using the try, except, and finally block.
"""

import sys

# car = {'make': 'Chevy', 'model': 'Silverado', 'year': '2006', 'color': 'Birch Metallic'}
car = {'make': 'Chevy', 'model': 'Silverado', 'year': '2006'}


def print_dict():
    try:
        # print("The make of your vehicle is: " + car['make'])
        # print("The model of your vehicle is: " + car['model'])
        # print("The year of your vehicle is: " + car['year'])
        print("The color of your vehicle is: " + car['color'])

    except Exception as e:
        print("\nAn exception occurred:  {0}".format(e))

    finally:
        print("\nHope you enjoy your vehicle.")


print_dict()
