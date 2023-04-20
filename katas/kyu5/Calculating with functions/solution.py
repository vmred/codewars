# This time we want to write calculations using functions and get the results.
# Let's have a look at some examples:

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3

# Requirements:
# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations:
# plus, minus, times, dividedBy (divided_by in Ruby and Python)
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Divison should be integer division. For example, this should return 2, not 2.666666...:


def expression(n, f):
    if not f:
        return n
    return f(n)


def zero(f=None):
    return expression(0, f)


def one(f=None):
    return expression(1, f)


def two(f=None):
    return expression(2, f)


def three(f=None):
    return expression(3, f)


def four(f=None):
    return expression(4, f)


def five(f=None):
    return expression(5, f)


def six(f=None):
    return expression(6, f)


def seven(f=None):
    return expression(7, f)


def eight(f=None):
    return expression(8, f)


def nine(f=None):
    return expression(9, f)


def plus(x):
    def f(y):
        return y + x

    return f


def minus(x):
    def f(y):
        return y - x

    return f


def times(x):
    def f(y):
        return y * x

    return f


def divided_by(x):
    def f(y):
        try:
            return int(y / x)
        except ZeroDivisionError:
            return False

    return f
