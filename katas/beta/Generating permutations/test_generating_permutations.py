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
import importlib
from asserts.asserts import assert_true

permutations = importlib.import_module('katas.beta.Generating permutations.solution').permutations


class TestSolution:
    def test_generating_permutations(self):
        results = {[tuple(p) for p in permutations([1, 2, 3])]}
        expected_results = {(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 2, 1), (3, 1, 2)}
        assert_true(expected_results, results)
