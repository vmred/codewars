# Find the missing letter

# Write a method that takes an array of consecutive (increasing) letters
# as input and that returns the missing letter in the array.

# You will always get an valid array. And it will be always exactly one letter be missing.
# The length of the array will always be at least 2.
# The array will always contain letters in only one case.

# Example:

# ['a','b','c','d','f'] -> 'e'
# ['O','Q','R','S'] -> 'P'
# (Use the English alphabet with 26 letters!)


def find_missing_letter(chars):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    is_upper = chars[0].istitle()
    chars = [i.lower() for i in chars]

    sl = alphabet[alphabet.index(chars[0]):alphabet.index(chars[len(chars) - 1]) + 1]

    diff = list(set(sl) - set(chars))[0]
    return diff.upper() if is_upper else diff
