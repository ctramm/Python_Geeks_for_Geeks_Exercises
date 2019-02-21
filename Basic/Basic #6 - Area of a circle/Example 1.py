# Area of a circle can simply be evaluated using the following formula
# Area = pi *(r * r)
# where r is radius of circle


def find_area_circle(r):
    PI = 3.142
    return PI * (r*r)


# Driver Code
radius = 5
print("Area is %.6f" % find_area_circle(radius))
