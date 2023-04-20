# Write a generator function named permutations that returns all permutations of the supplied list.

# This function cannot modify the list that is passed in, or modify the lists that it returns inbetween iterations.

# In Python a generator function is a function that uses the yield keyword
# instead of return to return an iterable set of results.

# example output:

# for p in permutations([1, 2, 3]):
#   print p

# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 2, 1]
# [3, 1, 2]


def permutations(l):
    elements_len = len(l)
    if elements_len <= 1:
        yield l
    else:
        for i in permutations(l[1:]):
            for j in range(elements_len):
                yield i[:j] + l[0:1] + i[j:]
