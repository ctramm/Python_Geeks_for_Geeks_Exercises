"""
Section 9: Finally and Else Block

Exceptions are errors
"""


def exception_handling():
    try:
        a = 10
        b = 20
        c = 0

        d = (a + b) / c
        print(d)

    except Exception as e:

        print("An error occurred.")
        print(e)
        raise Exception("This is an exception")

    else:
        print("No exception, else is executed.")

    finally:
        print("Finally, always executes.")


exception_handling()
