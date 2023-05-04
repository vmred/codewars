# Introduction and Warm-up (Highly recommended)
# Playing With Lists/Arrays Series
# Task
# Given an array/list [] of integers , Find The maximum difference between the successive elements in its sorted form.

# Notes
# Array/list size is at least 3 .
# Array/list's numbers Will be mixture of positives and negatives also zeros_
# Repeatition of numbers in the array/list could occur.
# The Maximum Gap is computed Regardless the sign.

# Input >> Output Examples
# maxGap ({13,10,5,2,9}) ==> return (4)


def max_gap(numbers):
    numbers = sorted(numbers)
    return max(numbers[i] - numbers[i - 1] for i in range(1, len(numbers)))
