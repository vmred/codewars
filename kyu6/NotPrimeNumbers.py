# You are given two positive integers a and b (a < b <= 20000).
# Complete the function which returns a list of all those numbers in the interval [a, b)
# whose digits are made up of prime numbers (2, 3, 5, 7) but which are not primes themselves.

# Be careful about your timing!


from asserts.Asserts import assert_true


def not_primes(a, b):
    def is_prime(n):
        if not n % 2 and n > 2:
            return False

        return all(n % i for i in range(3, int(n ** 0.5) + 1, 2))

    arr = [x for x in range(a, b) if all(i in {'2', '3', '5', '7'} for i in str(x))]
    return [x for x in arr if not is_prime(x)]

    # primes = [x for x in range(a, b) if not is_prime(x)]
    # return [x for x in primes if all(i in str(x) for i in s)]


assert_true(not_primes(2, 222), [22, 25, 27, 32, 33, 35, 52, 55, 57, 72, 75, 77])
assert_true(not_primes(2, 77), [22, 25, 27, 32, 33, 35, 52, 55, 57, 72, 75])
assert_true(not_primes(2700, 3000),
            [2722, 2723, 2725, 2727, 2732, 2733, 2735, 2737, 2752, 2755, 2757, 2772, 2773, 2775])
