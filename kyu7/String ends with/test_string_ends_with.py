from asserts.asserts import assert_true
import importlib

solution = importlib.import_module('kyu7.String ends with.solution').solution


class TestSolution:
    def test_string_ends_with(self):
        assert_true(solution('abcde', 'abc'), False)
