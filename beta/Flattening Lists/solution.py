# In this Kata you will create a function that takes a list of lists as an input and returns a flattened list.
# Note that if there are more lists inside these lists, they should not be flattened.

# Example:
# flatten [[1,2],[3,4]] == [1,2,3,4]
# flatten [[1],[2],[3],[4]] == [1,2,3,4]
from functools import reduce


def flatten(l):
    return reduce(lambda x, y: x + y, l)
