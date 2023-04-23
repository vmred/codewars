# Count the number of occurrences of each character and return it as a list of tuples in order of appearance.

# Example:
# ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]


def ordered_count(input):
    v = []
    for i in input:
        if i not in v:
            v.append(i)
    return [(i, input.count(i)) for i in v]
