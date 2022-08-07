"""
You and your friends are all fans of the hit TV show ThroneWorld and like to discuss it on social media. Unfortunately, some of your friends don't watch every new episode the minute it comes out. Out of consideration for them you would like to obfuscate your status updates so as to keep them spoiler-free.

You settle on a route cipher, which is a type of transposition cipher. Given a message and a number of rows and number of columns, to compute the route encryption of the message:

 - Write out the message row-wise in a grid of size rows by cols
 - then read the message column-wise.

You are guaranteed that rows * cols == len(message).

Your task is to write a function that, given a message, rows, and cols, returns the route encryption of the message.

Example:

message1 = "One does not simply walk into Mordor", rows1 = 6, cols1 = 6

O n e   d o
e s   n o t
  s i m p l
y   w a l k
  i n t o
M o r d o r

transpose(message1, rows1, cols1) -> "Oe y Mnss ioe iwnr nmatddoploootlk r"

Other examples:

message2 = "1.21 gigawatts!", rows2 = 5, cols2 = 3
1 . 2
1   g
i g a
w a t
t s !

transpose(message2, rows2, cols2) -> "11iwt. gas2gat!"

message2 = "1.21 gigawatts!", rows3 = 3, cols3 = 5
transpose(message2, rows3, cols3) -> "1ga.it2gt1as w!"

All Test Cases:
transpose(message1, rows1, cols1) -> "Oe y Mnss ioe iwnr nmatddoploootlk r"
transpose(message2, rows2, cols2) -> "11iwt. gas2gat!"
transpose(message2, rows3, cols3) -> "1ga.it2gt1as w!"

Complexity analysis:

n: the length of the message
"""
message1 = "One does not simply walk into Mordor"
rows1, cols1 = 6, 6

count = 0


def transpose(message, row, col):
    my_list = []
    for i, char in enumerate(message):
        if len(message) == row:
            my_list[i].append([])
        elif len(message):

        else:
            my_list.append(char)
    # [print(i, end=' ') for i in my_list]
    print(my_list)
    # output function


transpose(message1, rows1, cols1)



