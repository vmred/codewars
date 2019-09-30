# Definition
# Strong number is the number that the sum of the factorial of its digits is equal to number itself.

# For example: 145, since
# 1! + 4! + 5! = 1 + 24 + 120 = 145
# So, 145 is a Strong number.

# Task
# Given a number, Find if it is Strong or not.

# Warm-up (Highly recommended)
# Playing With Numbers Series

# Notes
# Number passed is always Positive.
# Return the result as String

# Input >> Output Examples
# strong_num(1) ==> return 'STRONG!!!!'
from math import factorial


def strong_num(number):
    return 'STRONG!!!!' if number == sum(factorial(int(i)) for i in str(number)) else 'Not Strong !!'
