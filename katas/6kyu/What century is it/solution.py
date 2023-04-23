# Return the inputted numerical year in century format. For example 2014, would return 21st.

# The input will always be a 4 digit string. So there is no need for year string validation

# Examples:
# Input: 1999 Output: 20th
# Input: 2011 Output: 21st
# Input: 2154 Output: 22nd
# Input: 2259 Output: 23rd
# Input: 1124 Output: 12th
# Input: 2000 Output: 20th


def whatCentury(year):
    suffix = {1: 'st', 2: 'nd', 3: 'rd'}
    century = (int(year) + 99) // 100

    if 10 <= century % 100 <= 20:
        suffix = 'th'
    else:
        suffix = suffix.get(century % 10, 'th')

    return str(century) + suffix