"""
Section 9: Practice Exercise Solution
"""


def exception_handling():
    try:
        car = {'make': 'bmw', 'model': '550i', 'year': '2016'}
        print(car['color'])
    except Exception as e:
        print("Key not found")
        print(e.with_traceback())
    finally:
        print("Finally, always executed.")


exception_handling()
