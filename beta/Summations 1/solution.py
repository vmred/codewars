# Make a program that will take an int (x) and give you the summation of all numbers from 1 up to x included.
# If the given input is not an integer, return "Invalid Value".

# Examples:
# summation(25)==325
# summation(2.56)=="Invalid Value"


def summation(x):
    if not isinstance(x, int):
        return 'Invalid Value'
    return sum(range(x + 1))
