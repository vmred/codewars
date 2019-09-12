# Write an algorithm that takes an array and moves all of the zeros to the end,
# preserving the order of the other elements.


def move_zeros(array):
    zeros_count = 0
    r = []

    for i in array:
        if i != 0 or i is False:
            r.append(i)
        else:
            zeros_count += 1

    return r + [0] * zeros_count

    # one line solution
    # return sorted(array, key=lambda x: x == 0 and x is not False)
