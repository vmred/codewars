# Definition
# A Tidy number is a number whose digits are in non-decreasing order.

# Task
# Given a number, Find if it is Tidy or not .

# Notes
# Number passed is always Positive .
# Return the result as a Boolean

# Input >> Output Examples
# tidyNumber (12) ==> return (true)
# Explanation:
# The number's digits { 1 , 2 } are in non-Decreasing Order (i.e) 1 <= 2 .

# tidyNumber (32) ==> return (false)
# Explanation:
# The Number's Digits { 3, 2} are not in non-Decreasing Order (i.e) 3 > 2 .

# tidyNumber (1024) ==> return (false)
# Explanation:
# The Number's Digits {1 , 0, 2, 4} are not in non-Decreasing Order as 0 <= 1 .
from asserts.Asserts import assert_true


def tidyNumber(n):
    n = str(n)
    for i in range(0, len(n) - 1):
        if n[i] > n[i + 1]:
            return False

    return True


assert_true(tidyNumber(102), False)
assert_true(tidyNumber(9672), False)
assert_true(tidyNumber(2789), True)
