# Definition
# Jumping number is the number that All adjacent digits in it differ by 1.

# Task
# Given a number, Find if it is Jumping or not .

# Warm-up (Highly recommended)
# Playing With Numbers Series
# Notes
# Number passed is always Positive .

# Return the result as String .
# The difference between ‘9’ and ‘0’ is not considered as 1 .
# All single digit numbers are considered as Jumping numbers.

# Input >> Output Examples
# jumpingNumber(9) ==> return "Jumping!!"


def jumping_number(number):
    number = list(map(int, str(number)))
    return ['Jumping!!', 'Not!!'][any(abs(number[x - 1] - number[x]) != 1 for x in range(1, len(number)))]
