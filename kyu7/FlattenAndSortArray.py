def flatten_and_sort(array):
    r = []
    for i in array:
        r += i

    return sorted(r)


a = flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]])
e = [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert (a == e), '--> actual: %s, expected %s' % (a, e)
