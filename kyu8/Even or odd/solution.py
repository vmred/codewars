# Create a function (or write a script in Shell) that takes an integer as an argument
# and returns "Even" for even numbers or "Odd" for odd numbers.
from asserts.asserts import assert_true


def even_or_odd(number):
    return ['Even', 'Odd'][number % 2]


assert_true(even_or_odd(2), "Even")
