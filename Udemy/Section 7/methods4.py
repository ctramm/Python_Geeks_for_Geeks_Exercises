"""
Section 7: Understanding Variable Scope


"""

a = 10


def method(a):
    print("Value of local 'a' is:" + str(a))
    a = 2
    print("New value of local 'a' is: " + str(a))


print("Value of global 'a' is: " + str(a))
method(a)
print("Did the value of global 'a' change? " + str(a))
print('#*' * 20)
b = 10


def method():
    global b
    print("Value of 'b' inside the method is:" + str(b))
    b = 2
    print("New value of 'b' inside the method is changed to: " + str(b))


print("Value of global 'b' is: " + str(b))
method()
print("Did the value of global 'b' change? " + str(b))
