import importlib
from asserts.asserts import assert_true

solution = importlib.import_module('katas.7kyu.String ends with.solution').solution


class TestSolution:
    def test_string_ends_with(self):
        assert_true(solution('abcde', 'abc'), False)
