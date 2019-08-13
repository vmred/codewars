# What's in a name?
# ..Or rather, what's a name in? For us, a particular string is where we are looking for a name.
# Task
# Test whether or not the string contains all of the letters which spell a given name, in order.

# The format
# A function passing two strings, searching for one (the name) within the other.
# ``function nameInStr(str, name){ return true || false }``
# Examples
# nameInStr('Across the rivers', 'chris') --> true
#             ^      ^  ^^   ^
# c      h  ri   s

# Contains all of the letters in 'chris', in order.
# nameInStr('Next to a lake', 'chris') --> false

# Contains none of the letters in 'chris'.
# nameInStr('Under a sea', 'chris') --> false
#                ^   ^
#                r   s

# Contains only some of the letters in 'chris'.
# nameInStr('A crew that boards the ship', 'chris') --> false
#              cr    h              s i
#              cr                h  s i
#              c     h      r       s i
#              ...

# Contains all of the letters in 'chris', but not in order.
# nameInStr('A live son', 'Allison') --> false
#            ^ ^^   ^^^
#            A li   son

# Contains all of the correct letters in 'Allison', in order,
# but not enough of all of them (missing an 'l').
from asserts.Asserts import assert_true


def name_in_str(s, name):
    def find_betweens_value(prev, arr, next):
        r = 0
        next = next[0] if len(next) == 1 else max(next)
        for v in arr:
            if prev < v <= next:
                r = v
        return r

    s = list(s.replace(' ', ''))

    if not all(i in s for i in name):
        return False

    # indexes of every char in name
    indexes = [[i for i, v in enumerate(s) if v == x] for x in name]
    # print('--> indexes:', indexes)
    r_i = []

    # trying to get array of ascending indexes
    for i in range(0, len(indexes)):
        if len(indexes[i]) == 1:
            r_i.append(indexes[i][0])

        else:
            r_i.append(
                find_betweens_value(r_i[i - 1], indexes[i], indexes[i + 1] if i < len(indexes) - 1 else indexes[i]))

    # if array is ascending sorted, return true
    return r_i == sorted(r_i)


assert_true(name_in_str("Across the rivers", "chris"), True)
assert_true(name_in_str("A crew that boards the ship", "chris"), False)
assert_true(name_in_str("Next to a lake", "chris"), False)
