"""
Section 8: Create your own object

"""


class Car(object):

    def __init__(self, make, model='Silverado', year=2019):
        self.make_of_car = make
        self.model = model
        self.year = year


c1 = Car('Chevy')
print(c1.make_of_car)
print(c1.model)
print(c1.year)

c2 = Car('Ford', 'F150', 2006)
print("\n" + c2.make_of_car)
print(c2.model)
print(c2.year)

