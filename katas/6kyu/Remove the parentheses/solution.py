# Remove the parentheses
# In this kata you are given a string for example:

# "example(unwanted thing)example"
# Your task is to remove everything inside the parentheses as well as the parentheses themselves.

# The example above would return:

# "exampleexample"
# Notes
# Other than parentheses only letters and spaces can occur in the string.
# Don't worry about other brackets like "[]" and "{}" as these will never appear.
# There can be multiple parentheses.
# The parentheses can be nested.
import re


def remove_parentheses(s):
    ret = ''
    skip = 0
    for i in s:
        if i == '(':
            skip += 1
        elif i == ')' and skip > 0:
            skip -= 1
        elif skip == 0:
            ret += i
    return ret
