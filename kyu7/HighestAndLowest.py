# In this little assignment you are given a string of space separated numbers,
# and have to return the highest and lowest number.

# Example:

# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"


def high_and_low(numbers):
    numbers = sorted(list(int(i) for i in numbers.split()))

    return '{} {}'.format(numbers[-1], numbers[0])


assert high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6") == "542 -214"
