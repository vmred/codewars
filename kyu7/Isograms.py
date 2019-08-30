# An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string that contains only letters is an isogram.
# Assume the empty string is an isogram. Ignore letter case.

# is_isogram("Dermatoglyphics" ) == true
# is_isogram("aba" ) == false
# is_isogram("moOse" ) == false # -- ignore letter case
from asserts.Asserts import assert_true


def is_isogram(strng):
    return len(set(strng.lower())) == len(strng)


assert_true(is_isogram("Dermatoglyphics"), True)
