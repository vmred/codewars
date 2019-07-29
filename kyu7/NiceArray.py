# A Nice array is defined to be an array where for every value n in the array,
# there is also an element n-1 or n+1 in the array.


from asserts.Asserts import assert_true


def is_nice(arr):
    # if len(arr) > 0:
    #     for i in arr:
    #         if not (i + 1 in arr or i - 1 in arr):
    #             return False
    #
    #     return True
    # else:
    #     return False

    return len(arr) > 0 and all(i + 1 in arr or i - 1 in arr for i in arr)


assert_true(is_nice([2, 10, 9, 3]), True)
assert_true(is_nice([3, 4, 5, 7]), False)
