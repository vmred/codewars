# Write a function that accepts an array of 10 integers (between 0 and 9),
# that returns a string of those numbers in the form of a phone number.

# Example:
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.


def create_phone_number(n):
    n = list(map(str, n))
    return '({}) {}-{}'.format(''.join(n[:3]), ''.join(n[3:6]), ''.join(n[6:]))
