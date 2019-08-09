# Complete the solution so that it returns true
# if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:
# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false
from asserts.Asserts import assert_true


def solution(string, ending):
    return string.endswith(ending)


assert_true(solution('abcde', 'abc'), False)
