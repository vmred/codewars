# Given a non-negative number, return the next bigger polydivisible number,
# or an empty value like null or Nothing.

# A number is polydivisible if its first digit is cleanly divisible by 1, its first two digits by 2,
# its first three by 3, and so on. There are finitely many polydivisible numbers.


def find_polydivisible(base=10):
    numbers = []
    previous = []
    for i in range(1, base):
        previous.append(i)
    new = []
    digits = 2
    while not previous == []:
        numbers = numbers + previous
        for i in range(0, len(previous)):
            for j in range(0, base):
                number = previous[i] * base + j
                if number % digits == 0:
                    new.append(number)
        previous = new
        new = []
        digits = digits + 1
    return numbers


def next_num(n):
    polydivisible = find_polydivisible()
    if n >= polydivisible[-1]: return None
    a = polydivisible[min(range(len(polydivisible)), key=lambda i: abs(polydivisible[i] - n))]
    return a if a > n else polydivisible[polydivisible.index(a) + 1]
