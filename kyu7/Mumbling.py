# This time no story, no theory. The examples below show you how to write function accum:

# Examples:

# accum('abcd') -> 'A-Bb-Ccc-Dddd'
# accum('RqaEzty') -> 'R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy'
# accum('cwAt') -> 'C-Ww-Aaa-Tttt'
# The parameter of accum is a string which includes only letters from a..z and A..Z
from asserts.Asserts import assert_true


def accum(s):
    return '-'.join([l.upper() + l.lower() * i for i, l in enumerate(s)])


assert_true(accum('ZpglnRxqenU'), 'Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu')
