# There is an array with some numbers. All numbers are equal except for one. Try to find it!

# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains more than 3 numbers.

# The tests contain some very huge arrays, so think about performance.
from functools import reduce

from asserts.Asserts import assert_true


def find_uniq(arr):
    s = set(arr)
    for i in s:
        if arr.count(i) == 1:
            return i


assert_true(find_uniq([1, 1, 1, 2, 1, 1]), 2)
assert_true(find_uniq([3, 4, 4, 4, 4, 4, 4, 4]), 3)
