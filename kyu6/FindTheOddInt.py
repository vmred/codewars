# Given an array, find the int that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.
from asserts.Asserts import assert_true


def find_it(seq):
    r = 0
    for i in seq:
        r ^= i
        print('--> r:', r)

    return r


assert_true(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]), 5)
