"""
Section 8: Create Your Own Methods
"""


class Car(object):

    def __init__(self, make, model, wheels=4):
        self.make = make
        self.model = model
        self.wheels = wheels

    def info(self):
        print("\nMake of the car: " + self.make)
        print("Model of the car: " + self.model)
        print("The car has " + str(self.wheels) + " wheels.")


c1 = Car('bmw', '550i', 6)
c1.info()

c2 = Car('benz', 'E350')
c2.info()
