# Given an input of an array of digits num, return the array with each digit incremented by its position in the array.
# For example, the first digit will be incremented by 1, the second digit by 2 etc.
# Make sure to start counting your positions from 1 and not 0.

# incrementer([1,2,3]) => [2,4,6]
# Your result can only contain single digit numbers,
# so if adding a digit with it's position gives you a multiple-digit number,
# only the last digit of the number should be returned

# incrementer([4,6,9,1,3]) => [5,8,2,5,8]

# - 9 + 3 (position of 9 in array) = 12
# - Only its last digit 2 should be returned
# Lastly, return [] if your array is empty! Arrays will only contain numbers so don't worry about checking that.
from asserts.Asserts import assert_true


def incrementer(nums):
    return [(x[1] + x[0] + 1) % 10 for x in enumerate(nums)]

    # r = []

    # for x in range(0, len(nums)):
    #     print('--> x: {}, index of x:{}, increment: {}'.format(x, nums.index(x), nums.index(x) + 1))
    #     inc = nums.index(x) + 1
    #     v = str(x + inc)
    #     if len(v) < 2:
    #         r.append(int(v))
    #
    #     else:
    #         r.append(int(v[-1]))
    #
    # return r


# assert_true(incrementer([1, 2, 3]), [2, 4, 6])
assert_true(incrementer([3, 6, 9, 8, 9]), [4, 8, 2, 2, 4])
