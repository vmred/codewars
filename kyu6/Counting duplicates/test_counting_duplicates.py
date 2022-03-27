from asserts.asserts import assert_true
import importlib

duplicate_count = importlib.import_module('kyu6.Counting duplicates.solution').duplicate_count


class TestSolution:
    def test_counting_duplicates(self):
        assert_true(duplicate_count('abcdea'), 1)
        assert_true(duplicate_count('abcdeaB'), 2)
