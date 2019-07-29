# Definition
# Extra perfect number is the number that first and last bits are set bits.

# Task
# Given a positive integer N , Return the extra perfect numbers in range from 1 to N .


def extra_perfect(n):
    return list(range(1, n + 1, 2))
