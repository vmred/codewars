# According to Wikipedia,
# a palindrome is "a word, phrase, number, or other sequence of characters which reads the same backward or forward."
# Examples of palindromes include "racecar", "tacocat", and "123454321".

# Capitalization, punctuation, and word dividers will be ignored when checking if a string is a palindrome.
# For example, "Was it a car or a cat I saw?" is a valid palindrome in context of this Kata.

# All requirements from definition should be fulfilled.
# If the given string is a palindrome, return true.
# If not, or in case of null input (None for Python) return false.


def is_palindrome(s):
    if not s:
        return False

    s = ''.join(i for i in s.lower() if i.isalnum())
    return s == s[::-1]
