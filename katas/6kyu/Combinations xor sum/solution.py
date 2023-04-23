# Given an array A and an integer x, map each element in the array to F(A[i],x)
# then return the xor sum of the resulting array.

# where F(n,x) is defined as follows:
# F(n, x) = xCx + x+1Cx + x+2Cx + ... + nCx
# and nCx represents Combination in mathematics

# Example
# a = [7, 4, 11, 6, 5]
# x = 3
# after mapping, `a` becomes [F(7,3), F(4,3), F(11,3), F(6,3), F(5,3)]
# return F(7,3) ^ F(4,3) ^ F(11,3) ^ F(6,3) ^ F(5,3)
# => 384
from math import factorial
from functools import reduce
from operator import xor


def transform(arr, x):
    def ncr(n, r):
        return factorial(n) // (factorial(r) * factorial(n - r))

    def f(a, b):
        return sum(ncr(i, b) for i in range(b, a + 1))

    return reduce(xor, [f(i, x) for i in arr])
