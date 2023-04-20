# Your task is to sort a given string. Each word in the string will contain a single number.
# This number is the position the word should have in the result.
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
# If the input.txt string is empty, return an empty string.
# The words in the input.txt String will only contain valid consecutive numbers.


def order(sentence):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    l = sentence.split()
    res = []
    for i in numbers:
        for k, m in enumerate(l):
            if i in m:
                res.append(l[k])
    return ' '.join(res)