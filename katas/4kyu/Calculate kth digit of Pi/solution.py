# The simple task
# You have to calculate k-th digit of π, knowing that:

# π = 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342...
# Make sure to check the anti-cheat rules at the bottom.

# Examples
# For k = 0:
# 3.14159265358979323...
# ^
# For k = 6:
# 3.14159265358979323...
#        ^

# Constraints
# 0 <= k < 10000

# Random test cases
# 1000 tests where 0 <= k < 10000

# Anti-cheat
# The only import allowed in Python is math
# The code length is limited to 2000 characters.
# Words http, www, requests, gmpy2 and search are banned.
# Eval and exec are banned
# Only ASCII characters are allowed


# def pi(k):
#     """Compute the kth digit of Pi using the BBP formula."""
#     p = 0
#     for i in range(k + 1):
#         p += (1 / pow(16, i)) * ((4 / (8 * i + 1)) - (2 / (8 * i + 4)) - (1 / (8 * i + 5)) - (1 / (8 * i + 6)))
#         print(i, p)
#     p = p - int(p)
#     return int(p * 16)


# pi = lambda n, r=3, a=0, b=1, c=1, d=1, e=3, f=3, i=0: i > n and r or pi(n, e, *
# [((2 * b + a) * f, b * d, c * f, d + 1, (b * (7 * d) + 2 + (a * f)) / (c * f), f + 2, i),
#  (10 * (a - e * c), 10 * b, c, d, ((10 * (3 * b + a)) / c) - 10 * e, f, i + 1)][4 * b + a - c < e * c])

def pi(n):
    a = i = 0
    b = c = d = 1
    r = e = f = 3
    while i <= n:
        r = e
        if 4 * b + a - c < e * c:
            g = 10 * (a - e * c)
            e = ((10 * (3 * b + a)) / c) - 10 * e
            b *= 10
            i += 1
        else:
            g = (2 * b + a) * f
            h = (b * (7 * d) + 2 + (a * f)) / (c * f)
            b *= d
            c *= f
            f += 2
            d += 1
            e = h
        a = g
        # print(r)
    return r
