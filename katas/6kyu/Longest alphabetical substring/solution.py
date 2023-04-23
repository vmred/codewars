# Find the longest substring in alphabetical order.

# Example: the longest alphabetical substring in "asdfaaaabbbbcttavvfffffdf" is "aaaabbbbctt".
# There are tests with strings up to 10 000 characters long so your code will need to be efficient.
# The input will only consist of lowercase characters and will be at least one letter long.
# If there are multiple solutions, return the one that appears first.

# Good luck :)


def longest(s):
    result = ''
    temp = ''

    for char in s:
        if not temp or temp[-1] <= char:
            temp += char
        elif temp[-1] > char:
            if len(result) < len(temp):
                result = temp
            temp = char

    if len(temp) > len(result):
        result = temp

    return result
