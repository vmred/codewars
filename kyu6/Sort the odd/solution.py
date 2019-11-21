# You have an array of numbers.
# Your task is to sort ascending odd numbers but even numbers must be on their places.

# Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

# Example

# sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]


def sort_array(source_array):
    result = sorted([i for i in source_array if i % 2])
    for i, v in enumerate(source_array):
        if not v % 2:
            result.insert(i, v)
    return result
