# There is an implementation of quicksort algorithm.
# Your task is to fix it.
# All inputs are correct.
# See also: https://en.wikipedia.org/wiki/Quicksort


def quicksort(arr):
    if len(arr) < 2:
        return arr  # base case

    p = arr[0]
    return quicksort([i for i in arr[1:] if i <= p]) + [p] + quicksort([i for i in arr[1:] if i > p])
