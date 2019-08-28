# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, and u as vowels for this Kata.
# The input string will only consist of lower case letters and/or spaces.
from asserts.Asserts import assert_true


def getCount(strng):
    def is_vowel(ch):
        return True if ch in ['a', 'e', 'i', 'o', 'u'] else False

    count = 0

    for i in strng:
        if is_vowel(i):
            count += 1

    return count


assert_true(getCount("abracadabra"), 5)
