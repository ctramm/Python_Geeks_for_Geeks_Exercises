"""
Bite 16 PyBites date generator

Write a generator that returns every 100th day counting forward from the PYBITES_BORN date.

Here is how the generator would work if you import and use it in your REPL.
from itertools import islice
from pprint import pprint as pp
from gendates import gen_special_pybites_dates
gen = gen_special_pybites_dates()
pp(list(islice(gen, 5)))
[datetime.datetime(2017, 3, 29, 0, 0),
 datetime.datetime(2017, 7, 7, 0, 0),
 datetime.datetime(2017, 10, 15, 0, 0),
 datetime.datetime(2018, 1, 23, 0, 0),
 datetime.datetime(2018, 5, 3, 0, 0)]
"""