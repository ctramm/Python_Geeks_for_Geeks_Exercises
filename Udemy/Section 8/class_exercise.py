"""
Section 8: Practice Exercise

Problem:
Create a Fruit class
    def 3 methods (init, nutrition, fruit_shape)
    print anything you like in these methods
Create Banana class that inherits from Fruit
    def 3 methods (init, nutrition, color)
    print anything you like in these methods

Create instances of classes, call methods from them.
"""


class Fruit(object):

    def __init__(self):
        print("I am a fruit.")

    def nutrition(self):
        print("Fruit is nutritious.")

    @staticmethod
    def fruit_shape():
        print("Fruits come in many shapes.")


class Banana(Fruit):

    def __init__(self):
        Fruit.__init__(self)
        print("Specifically, I am a banana.")

    def nutrition(self):
        super(Banana, self).nutrition()
        print("One serving of banana contains 110 calories, 30g of carbs, and 1g of protein.")

    @staticmethod
    def color():
        print("Bananas can be green, yellow, or brown. They are most delicious when yellow.")


apple = Fruit()
apple.nutrition()
apple.fruit_shape()

print("\n")

b = Banana()
b.fruit_shape()
b.nutrition()
b.color()
