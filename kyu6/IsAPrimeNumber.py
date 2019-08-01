# Define a function that takes an integer argument and returns logical value true or false
# depending on if the integer is a prime.

# Per Wikipedia, a prime number (or a prime) is a natural number greater than 1
# that has no positive divisors other than 1 and itself.

# Example
# is_prime(1)  /* false */
# is_prime(2)  /* true  */
# is_prime(-1) /* false */
from asserts.Asserts import assert_true


def is_prime(num):
    return num > 1 and not any(num % n == 0 for n in range(2, num))


assert_true(is_prime(75), False)
