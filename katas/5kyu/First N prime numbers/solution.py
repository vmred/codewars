# First N prime numbers
# A prime number is an integer greater than 1 that is only evenly divisible by itself and 1.
# Write your own Primes class with class method Primes.first(n) that returns an array of the first n prime numbers.

# For example:
# Primes.first(1)
# => [2]

# Primes.first(2)
# => [2, 3]

# Primes.first(5)
# => [2, 3, 5, 7, 11]

# Primes.first(20).last(5)
# => [53, 59, 61, 67, 71]


def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


class Primes:
    d = dict()

    @staticmethod
    def first(n):
        result = []
        i = 2
        while len(result) < n:
            if i in Primes.d:
                prime = Primes.d[i]
            else:
                prime = is_prime(i)
                Primes.d[i] = prime
            if prime:
                result.append(i)
            i += 1
        return result
