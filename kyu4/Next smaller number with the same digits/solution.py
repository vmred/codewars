# Write a function that takes a positive integer
# and returns the next smaller positive integer containing the same digits.

# For example:
# next_smaller(21) == 12
# next_smaller(531) == 513
# next_smaller(2071) == 2017

# Return -1 (for Haskell: return Nothing), when there is no smaller number that contains the same digits.
# Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.

# next_smaller(9) == -1
# next_smaller(135) == -1
# next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
# some tests will include very large numbers.
# test data only employs positive integers.
# import itertools


def next_smaller(number):
    new_number = number
    digit = [int(i) for i in str(number)]
    digits = len(digit) - 1
    index_1 = digits - 1

    while index_1 >= 0:
        index_2 = digits
        while index_2 > index_1:
            if digit[index_2] < digit[index_1]:
                digit[index_2], digit[index_1] = digit[index_1], digit[index_2]
                _first = digit[0:index_1 + 1]
                _second = digit[index_1 + 1:]
                _second.sort(reverse=True)
                digit = _first + _second
                print('-->', digit)
                new_number = ''.join(str(i) for i in digit)
                if new_number.startswith('0'):
                    return -1

                return int(new_number)

            else:
                index_2 -= 1

        index_1 -= 1

    return -1 if new_number == number else new_number
