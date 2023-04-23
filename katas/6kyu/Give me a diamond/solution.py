# Jamie is a programmer, and James' girlfriend.
# She likes diamonds, and wants a diamond string from James.
# Since James doesn't know how to make this happen, he needs your help.

# Task
# You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters.
# Trailing spaces should be removed, and every line must be terminated with a newline character (\n).

# Return null/nil/None/... if the input is an even number or negative,
# as it is not possible to print a diamond of even or negative size.

# Examples
# A size 3 diamond:
#  *
# ***
#  *


def diamond(n):
    if not n or not n % 2 or n < 0:
        return None

    r = ''
    for i in range(n):
        line = '*' * (i * 2 + 1) if i <= n / 2 else '*' * ((n - i) * 2 - 1)
        r += ' ' * int((n - len(line)) / 2) + line + '\n'
    return r
