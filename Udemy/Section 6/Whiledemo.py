"""
Section 6: While Loop Demo

Execute statements repeatedly
Conditions are used to stop the execution of loops
Iterable items are Strings, List, Tuple, Dictionary
"""

# x = 0
# while x < 10:
#     print("Value of x is:" + str(x))
#     x += 1

my_list = []
num = 0
while num < 10:
    my_list.append(num)
    print("Value of num is: " + str(num))
    num += 1

print("\nPrint list outside of while loop")
print(my_list)


def american_flag():
    first_counter = 0

    while first_counter < 5:
        print("**********---------------")
        first_counter += 1

    second_counter = 0

    while second_counter < 4:
        print("-------------------------")
        second_counter += 1

if __name__ == "__main__":

    american_flag()
