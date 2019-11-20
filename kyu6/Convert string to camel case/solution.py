# Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized
# (known as Upper Camel Case, also often referred to as Pascal case).

# Examples
# to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

# to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"


def to_camel_case(text):
    if not text:
        return ''

    text = text.replace('-', ' ').replace('_', ' ').split(' ')
    result = [text[0]]

    for i in range(1, len(text)):
        result.append(text[i][0].upper() + text[i][1:])

    return ''.join(result)
