"""
Nested Dictionary:
d = {'k1': {'nestk1':'nestvalue1', 'nestk2': 'nestvalue2'}}
d['k1']['nestk1']
"""

cars = {'bmw': {'model': '550i', 'year': 2016}, 'benz': {'model': 'E350', 'year': 2015}}
bmw_year = cars['bmw']['year']
print(bmw_year)
print(cars['benz']['model'])


# I don't think this is an exmaple of nested dictionaries but I had fun making it.
make = ('chevy', 'ford', 'gmc', 'toyota')
model = ('1500', 'f150', 'sierra', 'tundra')
year = ('2019', '2018', '2017', '2016')

my_truck = year[3] + " " + make[0] + " " + model[0]
print(my_truck)
