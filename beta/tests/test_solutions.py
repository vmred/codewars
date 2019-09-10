from asserts.Asserts import assert_true
from beta.Generating_permutations.solution import permutations


class TestSolution:
    def test_generating_permutations(self):
        results = set([tuple(p) for p in permutations([1, 2, 3])])
        expected_results = set([(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 2, 1), (3, 1, 2)])
        assert_true(expected_results, results)
