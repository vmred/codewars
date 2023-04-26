from asserts.asserts import assert_true
import importlib

find_missing = importlib.import_module(
    'katas.6kyu.Find the missing term in an Arithmetic Progression.solution'
).find_missing


class TestSolution:
    def test_find_the_missing_term_in_an_arithmetic_progression(self):
        assert_true(find_missing([1, 2, 3, 4, 6, 7, 8, 9]), 5)
        assert_true(find_missing([1, 3, 4, 5, 6, 7, 8, 9]), 2)
