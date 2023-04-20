# Calculate the sum of all the arguments passed to a function.

# Note: If any of the arguments is not a finite number the function should return false/False
# instead of the sum of the arguments.


def sum_all(*args):
    try:
        return sum(args)
    except TypeError:
        return False
