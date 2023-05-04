# Task
# Given an array of N integers, you have to find how many times you have to add up the smallest numbers in the array
# until their Sum becomes greater or equal to K.

# Notes:
# List size is at least 3.
# All numbers will be positive.
# Numbers could occur more than once , (Duplications may exist).
# Threshold K will always be reachable.

# Input >> Output Examples
# minimumSteps({1, 10, 12, 9, 2, 3}, 6)  ==>  return (2)

# Explanation:
# We add two smallest elements (1 + 2), their sum is 3 .
# Then we add the next smallest number to it (3 + 3) , so the sum becomes 6 .
# Now the result is greater or equal to 6 , Hence the output is (2) i.e (2) operations are required to do this .
# minimumSteps({8 , 9, 4, 2}, 23)  ==> return (3)


def minimum_steps(numbers, value):
    numbers = sorted(numbers)

    s = 0
    for i, v in enumerate(numbers):
        s += v

        if s >= value:
            return i

    return None
