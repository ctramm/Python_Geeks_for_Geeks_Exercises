"""
Split up the message on newline using the split builtin, then use the join builtin to stich it together using a pipe.
So...
'Hello world:\nI am coding in Python :)\nHow awesome!' becomes...
'Hello world:|Iam coding in Python :)|How awesome!'
Your code should work for other message strings as well.
Note that as opposed to previous intro bites your need to return the new string!
Also note that, although we wanted you to learn about split and join here, there are more ways to pull this off.
"""


message = """Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""


def split_in_columns(msg=message):
    """Split the message by newline (\n) and join it together on '|'
       (pipe), return the obtained output string"""
    lines = msg.split('\n')
    return '|'.join(lines)
