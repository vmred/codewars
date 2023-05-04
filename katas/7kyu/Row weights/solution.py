# Scenario
# Several people are standing in a row divided into two teams.
# The first person goes into team 1, the second goes into team 2, the third goes into team 1, and so on.

# Task
# Given an array of positive integers (the weights of the people), return a new array/tuple of two integers,
# where the first one is the total weight of team 1, and the second one is the total weight of team 2.

# Notes
# Array size is at least 1.
# All numbers will be positive.

# Input >> Output Examples
# rowWeights([13, 27, 49])  ==>  return (62, 27)
# Explanation:
# The first element 62 is the total weight of team 1, and the second element 27 is the total weight of team 2.


def row_weights(array):
    if len(array) == 1:
        return array[0], 0

    s1 = 0
    s2 = 0
    for i, v in enumerate(array):
        if not i % 2:
            s1 += v
        else:
            s2 += v

    return s1, s2
