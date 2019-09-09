# Task:
# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...".
# Input will always be valid, i.e. no negative integers.


from asserts.Asserts import assert_true


def count_sheep(n):
    return ''.join(['{} sheep...'.format(x) for x in range(1, n + 1)])


assert_true(count_sheep(1), '1 sheep...')
assert_true(count_sheep(2), "1 sheep...2 sheep...")
