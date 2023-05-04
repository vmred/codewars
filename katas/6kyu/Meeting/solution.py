# John has invited some friends.
# His list is:

# s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
# Could you make a program that

# makes this string uppercase
# gives it sorted in alphabetical order by last name.
# When the last names are the same, sort them by first name.
# Last name and first name of a guest come in the result between parentheses separated by a comma.

# So the result of function meeting(s) will be:

# "(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"
# It can happen that in two distinct families with the same family name two people have the same first name too.

# Notes
# You can see another examples in the "Sample tests".


def meeting(s):
    def parse_string(value):
        value = value.split(';')
        r = []
        for item in value:
            item = item.split(':')
            r.append({'first_name': item[0].upper(), 'last_name': item[1].upper()})

        return r

    s = sorted(parse_string(s), key=lambda x: (x['last_name'], x['first_name']))

    # pylint: disable=consider-using-f-string
    return ''.join('({}, {})'.format(x["last_name"].replace("'", ""), x["first_name"]) for x in s)
