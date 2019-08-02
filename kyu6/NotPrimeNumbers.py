# You are given two positive integers a and b (a < b <= 20000).
# Complete the function which returns a list of all those numbers in the interval [a, b)
# whose digits are made up of prime numbers (2, 3, 5, 7) but which are not primes themselves.

# Be careful about your timing!
import math

from asserts.Asserts import assert_true


def not_primes(a, b):
    def is_prime(p):
        if p == 2: return True
        if p % 2 == 0: return False
        max = p ** 0.5 + 1
        i = 3
        while i <= max:
            if p % i == 0:
                return False
            i += 2
        return True

    # def is_prime(num):
    #     return num > 1 and not any(num % n == 0 for n in range(2, num))

    return [x for x in range(a, b) if not is_prime(x) and all(i in {'2', '3', '5', '7'} for i in str(x))]


assert_true(not_primes(2, 222), [22, 25, 27, 32, 33, 35, 52, 55, 57, 72, 75, 77])
# assert_true(not_primes(2700, 3000),
#             [2722, 2723, 2725, 2727, 2732, 2733, 2735, 2737, 2752, 2755, 2757, 2772, 2773, 2775])
