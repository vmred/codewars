# In this simple assignment you are given a number and have to make it negative.
# But maybe the number is already negative?

# Example:
# make_negative(1);  # return -1
# make_negative(-5); # return -5
# make_negative(0);  # return 0
from asserts.asserts import assert_true


def make_negative(number):
    return -number if number > 0 else number
