# ou are given an input string.

# For each symbol in the string if it's the first character occurence, replace it with a '1',
# else replace it with the amount of times you've already seen it...

# But will your code be performant enough?

# Examples:
# input   =  "Hello, World!"
# result  =  "1112111121311"

# input   =  "aaaaaaaaaaaa"
# result  =  "123456789101112"
# There might be some non-ascii characters in the string.


def numericals(s):
    seen = {}
    r = ''
    for i in s:
        seen[i] = seen.get(i, 0) + 1
        r += str(seen[i])

    return r
