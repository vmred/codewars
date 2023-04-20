# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then it should replace the missing second character
# of the final pair with an underscore ('_').

# Examples:

# solution('abc')  # should return ['ab', 'c_']
# solution('abcdef')  # should return ['ab', 'cd', 'ef']


def solution(s):
    r = []
    x = len(s)
    for i in range(1, x, 2):
        r.append(s[i - 1] + s[i])

    if x % 2:
        r.append('{}_'.format(s[-1]))

    return r
