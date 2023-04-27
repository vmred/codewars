# Given a lowercase string that has alphabetic characters only and no spaces,
# return the highest value of consonant substrings.
# Consonants are any letters of the alpahabet except "aeiou".

# We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

# For example, for the word "zodiacs", let's cross out the vowels. We get: "z o d ia cs"

# -- The consonant substrings are: "z", "d" and "cs" and the values are z = 26, d = 4 and cs = 3 + 19 = 22.
# The highest is 26.
# solve("zodiacs") = 26

# For the word "strength", solve("strength") = 57
# -- The consonant substrings are: "str" and "ngth" with values "str" = 19 + 20 + 18 = 57
# and "ngth" = 14 + 7 + 20 + 8 = 49. The highest is 57.
# For C: do not mutate input.

# More examples in test cases. Good luck!


def solve(s):
    d = {
        'b': 2,
        'c': 3,
        'd': 4,
        'f': 6,
        'g': 7,
        'h': 8,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26,
    }

    exceptions = ['a', 'e', 'i', 'o', 'u']
    substrings = []

    sl = ''
    for i in range(0, len(s)):
        if s[i] not in exceptions:
            sl += s[i]
        else:
            substrings.append(sl)
            sl = ''

        if i + 1 == len(s):
            substrings.append(sl)

    return max(sum(d[x] for x in subs) for subs in substrings)
    # return max(sum(ord(c) - 96 for c in subs) for subs in re.split('[aeiou]+', s))
