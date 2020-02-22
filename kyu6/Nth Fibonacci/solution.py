# I love Fibonacci numbers in general, but I must admit I love some more than others.

# I would like for you to write me a function that when given a number (n) and returns the n-th number
# in the Fibonacci Sequence.

# For example:
# nth_fib(4) == 2
# Because 2 is the 4th number in the Fibonacci Sequence.

# For reference, the first two numbers in the Fibonacci sequence are 0 and 1,
# and each subsequent number is the sum of the previous two.

def nth_fib(n):
    n = n - 1
    return ((1 + 5 ** 0.5) ** n - (1 - 5 ** 0.5) ** n) / (5 ** 0.5 * 2 ** n) // 1
