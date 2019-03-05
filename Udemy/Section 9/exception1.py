"""
Section 9: Exception Handling Demo

Exceptions are errors
We should handle exceptions in our code to make sure the code is working the way we
    want and is handling all the unwanted issues.
Link to 3.5 built-in exceptions - https://docs.python.org/3/library/exceptions.html
"""


def exception_handling():
    try:
        a = 10
        b = "20"
        c = 0

        d = (a + b) / c
        print(d)

    # except ZeroDivisionError as e:
    #     print("Zero Division Error.")
    #     print(e)
    #
    # except TypeError as e:
    #     print("Type Error: Can't add string to integer")
    #     print(e)
    except Exception as e:
        print("An error occurred.")
        print(e)


exception_handling()
