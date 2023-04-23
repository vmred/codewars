# ROT13 is a simple letter substitution cipher that replaces a letter
# with the letter 13 letters after it in the alphabet.
# ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13.
# If there are numbers or special characters included in the string, they should be returned as they are.
# Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
import string


def rot13(message):
    alphabet = list(string.ascii_lowercase)
    r = ''

    for i in message:
        if i.isalpha():
            c = i
            encoded = alphabet.index(c.lower()) + 13
            if encoded >= 26:
                encoded -= 26
            r += alphabet[encoded].upper() if i.isupper() else alphabet[encoded]
        else:
            r += i
    return r
