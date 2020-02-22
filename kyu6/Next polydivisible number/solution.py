# Given a non-negative number, return the next bigger polydivisible number,
# or an empty value like null or Nothing.

# A number is polydivisible if its first digit is cleanly divisible by 1, its first two digits by 2,
# its first three by 3, and so on. There are finitely many polydivisible numbers.
import sys


def next_num(n):
    if n > sys.maxsize:
        return None
    n = n + 1

    while True:
        str_n = str(n)
        if all(int(str_n[:i + 1]) % (i + 1) == 0 for i, _ in enumerate(str_n)):
            return n
        else:
            n += 1
