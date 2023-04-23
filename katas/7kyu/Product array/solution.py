# Task
# Given an array/list [] of integers , Construct a product array Of same size
# Such That prod[i] is equal to The Product of all the elements of Arr[] except Arr[i].

# Notes
# Array/list size is at least 2 .
# Array/list's numbers Will be only Positives
# Repetition of numbers in the array/list could occur.

# Input >> Output Examples
# productArray ({12,20}) ==>  return {20,12}
# Explanation:
# The first element in prod [] array 12 is the product of all array's elements except the first element
# The second element 20 is the product of all array's elements except the second element .

from functools import reduce


def product_array(numbers):
    return [reduce((lambda x, y: x * y), numbers[:i] + numbers[i + 1:]) for i in range(0, len(numbers))]
