# Definition
# A number is a Special Number if it’s digits only consist 0, 1, 2, 3, 4 or 5

# Given a number determine if it special number or not .

# Warm-up (Highly recommended)
# Playing With Numbers Series
# Notes
# The number passed will be positive (N > 0) .

# All single-digit numbers with in the interval [0:5] are considered as special number.

# Input >> Output Examples
# specialNumber(2) ==> return "Special!!"
from asserts.Asserts import assert_true


def special_number(number):
    return ['NOT!!', 'Special!!'][all(int(x) < 6 for x in str(number))]


assert_true(special_number(2), 'Special!!')
assert_true(special_number(39), "NOT!!")
assert_true(special_number(11350224), 'Special!!')
