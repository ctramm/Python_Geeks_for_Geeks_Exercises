"""
Section 8: Inheritance
"""


class Car(object):

    def __init__(self):
        print("You just created the car.")

    @staticmethod
    def drive():
        print("Car started moving...")

    @staticmethod
    def stop():
        print("Car stopped moving...")


class BMW(Car):

    def __init__(self):
        Car.__init__(self)
        print("You just created the BMW.")


c = Car()
c.drive()
c.stop()
print("#*" * 20)
b = BMW()
b.drive()
b.stop()

