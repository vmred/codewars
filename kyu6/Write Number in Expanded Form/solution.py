# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# NOTE: All numbers will be whole numbers greater than 0.

# If you liked this kata, check out part 2!!


def expanded_form(num):
    extensions = []

    while num != 0:
        l = len(str(num))
        if l > 1:
            v = int(str(num)[0]) * int('1' + '0' * (l - 1))
            extensions.append(v)
            num -= v
        else:
            extensions.append(num)
            break

    return ' + '.join(str(x) for x in extensions)
