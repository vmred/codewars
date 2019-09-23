# How many ways can you make the sum of a number?
# From wikipedia: https://en.wikipedia.org/wiki/Partition_(number_theory)#

# In number theory and combinatorics, a partition of a positive integer n,
# also called an integer partition, is a way of writing n as a sum of positive integers.
# Two sums that differ only in the order of their summands are considered the same partition.
# If order matters, the sum becomes a composition.

# For example, 4 can be partitioned in five distinct ways:
# 4
# 3 + 1
# 2 + 2
# 2 + 1 + 1
# 1 + 1 + 1 + 1

# Examples
# exp_sum(1) # 1
# exp_sum(2) # 2  -> 1+1 , 2
# exp_sum(3) # 3 -> 1+1+1, 1+2, 3
# exp_sum(4) # 5 -> 1+1+1+1, 1+1+2, 1+3, 2+2, 4
# exp_sum(5) # 7 -> 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3
# exp_sum(10) # 42


def exp_sum(n):
    parts = [1] + [0] * n
    for t in range(1, n + 1):
        for i, x in enumerate(range(t, n + 1)):
            parts[x] += parts[i]
    return parts[n]
