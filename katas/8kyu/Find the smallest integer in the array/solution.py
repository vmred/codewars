# Given an array of integers your solution should find the smallest integer.

# For example:
# Given [34, 15, 88, 2] your solution will return 2
# Given [34, -345, -1, 100] your solution will return -345
# You can assume, for the purpose of this kata, that the supplied array will not be empty.
from asserts.asserts import assert_true


def find_smallest_int(arr):
    return min(arr)


assert_true(find_smallest_int([0, 1 - 2**64, 2**64]), 1 - 2**64)
