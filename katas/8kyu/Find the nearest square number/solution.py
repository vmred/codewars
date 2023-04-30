# Your task is to find the nearest square number, nearest_sq(n), of a positive integer n.

# Good luck :)

import math


def nearest_sq(n):
    return pow(round(math.sqrt(n)), 2)
