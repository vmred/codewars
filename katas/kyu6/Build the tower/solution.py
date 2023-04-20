# Build Tower
# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).

# Tower block is represented as *

# Python: return a list;
# JavaScript: returns an Array;
# C#: returns a string[];
# PHP: returns an array;
# C++: returns a vector<string>;
# Haskell: returns a [String];
# Ruby: returns an Array;
# Have fun!


def tower_builder(n_floors):
    result = []
    stars = 1
    for i in range(1, n_floors + 1):
        result.append('*' * stars)
        stars += 2

    max_floor = len(result[-1])

    for i in range(0, len(result)):
        while len(result[i]) < max_floor:
            result[i] = ' {} '.format(result[i])

    return result
