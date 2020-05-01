# Task:
# Your function should return a valid regular expression.
# This is a pattern which is normally used to match parts of a string.
# In this case will be used to check if all the characters given in the input appear in a string.

# Input
# Non empty string of unique alphabet characters upper and lower case.

# Output
# Regular expression pattern string.

# Examples
# Your function should return a string.

# Function example
# def regex_contains_all(st):
#   return r"abc"
# That regex pattern will be tested like this.

# Test
# abc = 'abc'
# pattern = regex_contains_all(abc)
# st = 'zzzaaacccbbbzzz'
# bool(re.match(pattern, st), f"Testing if {st} contains all characters in {abc} with your pattern {pattern}") -> True


def regex_contains_all(st):
    return r"(?i)" + ''.join(["(?=.*{})".format(x) for x in st])
