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


def name_in_str(s, name):
    def find_betweens_value(prev, arr, next_el):
        r = 0
        next_el = next_el[0] if len(next_el) == 1 else max(next_el)
        for v in arr:
            if prev < v <= next_el:
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
    for i, v in enumerate(indexes):
        if len(v) == 1:
            r_i.append(v[0])

        else:
            r_i.append(find_betweens_value(r_i[i - 1], v, indexes[i + 1] if i < len(indexes) - 1 else v))

    # if array is ascending sorted, return true
    return r_i == sorted(r_i)
