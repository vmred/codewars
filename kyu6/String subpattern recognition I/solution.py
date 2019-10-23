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


def has_subpattern(text):
    for i in range(1, len(text) // 2 + 2):
        if len(text) % i == 0:
            subtext = text[:i]
            num_subtext = text.count(subtext)
            if num_subtext > 1 and num_subtext * len(subtext) == len(text):
                return True
    return False
    # one more solution:
    # return bool(re.search(r'^(\w+)\1+$', s))
    # and one more:
    # return (string * 2).find(string, 1) != len(string)
