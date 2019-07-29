# Write a function that takes an integer as input, and returns the number of bits that are equal to 1
# in the binary representation of that number. You can guarantee that input is non-negative.

# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case


def countBits(n):
    return bin(n)[2:].count('1')


a = countBits(10)
e = 2
assert (a == e), '--> actual: %s, expected %s' % (a, e)

a = countBits(1234)
e = 5
assert (a == e), '--> actual: %s, expected %s' % (a, e)
