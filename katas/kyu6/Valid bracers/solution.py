# Write a function that takes a string of braces, and determines if the order of the braces is valid.
# It should return true if the string is valid, and false if it's invalid.

# This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}.
# Thanks to @arnedag for the idea!

# All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

# What is considered Valid?
# A string of braces is considered valid if all braces are matched with the correct brace.


def validBraces(strng):
    while '()' in strng or '{}' in strng or '[]' in strng:
        strng = strng.replace('()', '').replace('{}', '').replace('[]', '')

    return len(strng) == 0
