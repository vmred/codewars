# Task
# Given an array of intgers , Find the minimum sum which is obtained from summing each Two integers product .

# Notes
# Array/list will contain positives only .
# Array/list will always has even size

# Input >> Output Examples
# minSum({5,4,2,3}) ==> return (22)
# Explanation:
# The minimum sum obtained from summing each two integers product , 5*2 + 3*4 = 22

# minSum({12,6,10,26,3,24}) ==> return (342)
# Explanation:
# The minimum sum obtained from summing each two integers product , 26*3 + 24*6 + 12*10 = 342
from asserts.Asserts import assert_true


def min_sum(arr):
    arr = sorted(arr)

    s = 0
    l = len(arr)
    for i in range(0, l):
        s += arr[i] * arr[l - 1 - i]

        if i == l - i - 2:
            return s

    return s


assert_true(min_sum([5, 4, 2, 3]), 22)
assert_true(min_sum([9, 2, 8, 7, 5, 4, 0, 6]), 74)
