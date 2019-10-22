# In this kata you need to build a function to return either true/True or false/False
# if a string can be seen as the repetition of a simpler/shorter subpattern or not.

# For example:

# has_subpattern("a") == False #no repeated pattern
# has_subpattern("aaaa") == True #created repeating "a"
# has_subpattern("abcd") == False #no repeated pattern
# has_subpattern("abababab") == True #created repeating "ab"
# has_subpattern("ababababa") == False #cannot be entirely reproduced repeating a pattern

# Strings will never be empty and can be composed of any character
# (just consider upper- and lowercase letters as different entities)
# and can be pretty long (keep an eye on performances!).


def has_subpattern(string):
    len_string = len(string)
    if len_string < 2:
        return False

    string_set = ''.join(sorted(set(string)))
    len_string_set = len(string_set)

    if string_set == string:
        return False

    for x in range(len(string[:len_string_set]), len_string):
        string_set = string[:x]
        len_string_set = len(string_set)
        for i in range(1, len_string_set + 1):
            pattern = string_set[:i]
            if pattern == string_set:
                if string.count(pattern) * len(pattern) == len_string:
                    return True

    return False
