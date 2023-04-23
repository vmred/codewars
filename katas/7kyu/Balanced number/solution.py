# Warm-up (Highly recommended)
# Playing With Numbers Series
# Notes
# If the number has an odd number of digits then there is only one middle digit,
# e.g. 92645 has middle digit 6; otherwise, there are two middle digits , e.g. 1301 has middle digits 3 and 0

# The middle digit(s) should not be considered when determining whether a number is balanced or not,
# e.g 413023 is a balanced number because the left sum and right sum are both 5.

# Number passed is always Positive .
# Return the result as String

# Input >> Output Examples
# balancedNum (7) ==> return "Balanced"
# Explanation:
# Since , The sum of all digits to the left of the middle digit (0)\
# and the sum of all digits to the right of the middle digit (0) are equal , then It's Balanced
# balancedNum (295591) ==> return "Not Balanced"


def balanced_num(number):
    number = [int(x) for x in str(number)]
    middle = [len(number) // 2] if len(number) % 2 else [len(number) // 2 - 1, len(number) // 2]
    return ['Not Balanced', 'Balanced'][len(number) < 3 or sum(number[:min(middle)]) == sum(number[max(middle) + 1:])]
