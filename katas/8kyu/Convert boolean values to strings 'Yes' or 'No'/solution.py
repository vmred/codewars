# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
from asserts.asserts import assert_true


def bool_to_word(boolean):
    return ['No', 'Yes'][boolean]


assert_true(bool_to_word(True), 'Yes')
