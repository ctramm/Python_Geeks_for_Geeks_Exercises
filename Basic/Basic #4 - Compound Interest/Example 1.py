# Formula to calculate compound interest annually is given by:
# Compound Interest = P( 1 +R /100)
# Where,
# P is principle amount
# R is the rate and
# T is the time span


# Function
def compound_interest(principle, rate, time):
    # Calculates Compound Interest
    CI = principle * (pow((1 + rate / 100), time))
    print("Compound interest is:", CI)


# Input
P = 1200
R = 5.4
T = 2

# Driver Code
compound_interest(P, R, T)
