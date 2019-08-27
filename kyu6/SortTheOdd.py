# You have an array of numbers.
# Your task is to sort ascending odd numbers but even numbers must be on their places.

# Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

# Example

# sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
from asserts.Asserts import assert_true


def sort_array(source_array):
    result = sorted([i for i in source_array if i % 2])
    for i, v in enumerate(source_array):
        if not v % 2:
            result.insert(i, v)
    return result


assert_true(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
assert_true(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
assert_true(sort_array([]), [])
assert_true(sort_array([1, 111, 11, 11, 2, 1, 5, 0]), [1, 1, 5, 11, 2, 11, 111, 0])
