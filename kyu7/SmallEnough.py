# You will be given an array and a limit value.
# You must check that all values in the array are below or equal to the limit value.
# If they are, return true. Else, return false.


def small_enough(array, limit):
    return False if any(i > limit for i in array) else True


print(small_enough([78, 117, 110, 99, 104, 117, 107, 115], 100))
