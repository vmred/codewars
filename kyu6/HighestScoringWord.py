# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.

from asserts.Asserts import assert_true


def high(x):
    x = x.split()
    s = 0
    word = ''

    for i in x:
        letters_sum = sum(ord(letter) - 96 for letter in i)
        if letters_sum > s:
            s = letters_sum
            word = i

    return word


assert_true(high('man i need a taxi up to ubud'), 'taxi')
