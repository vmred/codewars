# Given an array, find the int that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.


def find_it(seq):
    r = 0
    for i in seq:
        r ^= i
        print('--> r:', r)

    return r
