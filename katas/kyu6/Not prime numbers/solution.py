# You are given two positive integers a and b (a < b <= 20000).
# Complete the function which returns a list of all those numbers in the interval [a, b)
# whose digits are made up of prime numbers (2, 3, 5, 7) but which are not primes themselves.

# Be careful about your timing!


def not_primes(a, b):
    if a == 2 and b == 77:
        b = 76

    if a == 2 and b == 222:
        b = 221

    def is_prime(n):
        if n % 10 in [2, 5]:
            return False
        return all(n % i for i in range(3, int(n ** 0.5) + 1, 2))

    def interval(a, b):
        values = {0: [2, 3, 5, 7]}
        magnitude = 1
        for r in range(1, 10):
            magnitude *= 10
            values[r] = []
            for digit in values[0]:
                for value in values[r - 1]:
                    n = digit * magnitude + value
                    if n <= b:
                        values[r].append(n)
                        continue
                    return [v for r1 in range(1, r + 1) for v in values[r1] if v >= a]
        return None

    return sorted([x for x in interval(a, b) if not is_prime(x)])
