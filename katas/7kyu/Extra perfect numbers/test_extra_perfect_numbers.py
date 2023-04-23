from asserts.asserts import assert_true
import importlib

extra_perfect = importlib.import_module('katas.7kyu.Extra perfect numbers.solution').extra_perfect


class TestSolution:
    def test_extra_perfect_numbers(self):
        assert_true(extra_perfect(10), [1, 3, 5, 7, 9])
        assert_true(extra_perfect(20), [1, 3, 5, 7, 9, 11, 13, 15, 17, 19])
