# Welcome. In this kata, you are asked to square every digit of a number.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer
from asserts.Asserts import assert_true


def square_digits(num):
    num = list(map(int, str(num)))
    return int(''.join(str(i ** 2) for i in num))


assert_true(square_digits(9119), 811181)
