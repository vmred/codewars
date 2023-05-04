# Task:
# Your task is to write a function which returns the sum of following series upto nth term(parameter).

# Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
# Rules:
# You need to round the answer to 2 decimal places and return it as String.

# If the given value is 0 then it should return 0.00
# You will only be given Natural Numbers as arguments.

# Examples:
# SeriesSum(1) => 1 = "1.00"
# SeriesSum(2) => 1 + 1/4 = "1.25"
# SeriesSum(5) => 1 + 1/4 + 1/7 + 1/10 + 1/13 = "1.57"


def series_sum(n):
    r = 0
    for i in range(0, n):
        r += 1 / (1 + 3 * i)
    return '{:.2f}'.format(r)  # pylint: disable=consider-using-f-string
