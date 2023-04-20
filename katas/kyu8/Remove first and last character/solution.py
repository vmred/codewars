# It's pretty straightforward.
# Your goal is to create a function that removes the first and last characters of a string.
# You're given one parameter, the original string.
# You don't have to worry with strings with less than two characters.
from asserts.asserts import assert_true


def remove_char(s):
    return s[1:-1]


assert_true(remove_char('eloquent'), 'loquen')
assert_true(remove_char('ok'), '')
