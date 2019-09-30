# A Nice array is defined to be an array where for every value n in the array,
# there is also an element n-1 or n+1 in the array.


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
