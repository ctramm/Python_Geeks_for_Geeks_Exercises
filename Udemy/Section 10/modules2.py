"""
Section 10: Create Your own Modules

"""

import math
from math import sqrt
# import Udemy.Utils.car as car
# from Udemy.Utils import car
from Udemy.Utils.car import info


class ModulesDemo:

    @staticmethod
    def built_modules():
        print(math.sqrt(100))
        print(sqrt(144))

    @staticmethod
    def car_description():
        make = 'bmw'
        model = '550i'
        # car.info(make, model)
        info(make, model)


m = ModulesDemo()
# m.built_modules()

m.car_description()
