# Python program to check if the number provided by the user is an Armstrong number

# take input from the user
num = int(input("Enter a number:"))

# initialize sum
sum = 0

length = len(str(num))

# find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** length
    temp //= 10

# display the result
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")



