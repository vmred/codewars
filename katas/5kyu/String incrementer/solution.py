# Your job is to write a function which increments a string, to create a new string.

# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.

# Examples:
# foo -> foo1
# foobar23 -> foobar24
import re


def increment_string(s):
    nums = re.findall(r'\d+', s)
    if nums:
        numb = nums[-1]
        s = s.rsplit(numb, 1)[0]
        number = str(int(numb) + 1)
        return s + '0' * (len(numb) - len(number)) + number
    return s + '1'
