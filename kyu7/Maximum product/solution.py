# Given an array of integers , Find the maximum product obtained from multiplying 2 adjacent numbers in the array.

# Notes
# Array/list size is at least 2.
# Array/list numbers could be a mixture of positives, negatives also zeroes .

# Input >> Output Examples
# adjacentElementsProduct([1, 2, 3]); ==> return 6


def adjacent_element_product(array):
    if len(array) == 1:
        return array[0]

    m = array[0] * array[1]

    for x in range(1, len(array)):
        if array[x - 1] * array[x] > m:
            m = array[x - 1] * array[x]

    return m
    # return max(a * b for a, b in zip(array, array[1:]))
