# Given a number, return a string with dash'-'marks before and after each odd integer,
# but do not begin or end the string with a dash mark.

# Ex:
# dashatize(274) -> '2-7-4'
# dashatize(6815) -> '68-1-5'
import re


def dashatize(num):
    try:
        return '-'.join(list(filter(None, re.split("([13579])", str(abs(num))))))
    except TypeError:
        return 'None'
