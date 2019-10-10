# In this kata, you've to count lowercase letters in a given string and return the letter count
# in a hash with 'letter' as key and count as 'value'. '
from collections import Counter


def letter_count(s):
    return Counter(s)
