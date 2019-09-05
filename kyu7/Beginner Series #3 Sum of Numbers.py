# Given two integers a and b, which can be positive or negative,
# find the sum of all the numbers between including them too and return it.
# If the two numbers are equal return a or b.

# Note: a and b are not ordered!
from asserts.Asserts import assert_true


def get_sum(a, b):
    if a > b:
        a, b = b, a

    return sum(i for i in range(a, b + 1))


assert_true(get_sum(0, -1), -1)
assert_true(get_sum(0, 1), 1)
