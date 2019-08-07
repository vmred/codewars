# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.
from asserts.Asserts import assert_true


def find_short(s):
    return len(sorted(s.split(' '), key=len)[0])


assert_true(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
assert_true(find_short("Lets all go on holiday somewhere very cold"), 2)
