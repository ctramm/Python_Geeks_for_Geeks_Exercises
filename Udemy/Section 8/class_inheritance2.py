"""
Section 8: Method Overriding
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

    def drive(self):
        super(BMW, self).drive()
        print("You are driving a BMW, Enjoy...")

    @staticmethod
    def headsup_display():
        print("This is a unique feature.")


# c = Car()
# c.drive()
# c.stop()
# print("#*" * 20)
b = BMW()
b.drive()
b.stop()
b.headsup_display()

