import importlib
from asserts.asserts import assert_true

solution = importlib.import_module('katas.6kyu.Split strings.solution').solution


class TestSolution:
    def test_split_strings(self):
        assert_true(solution('asdfadsf'), ['as', 'df', 'ad', 'sf'])
        assert_true(solution("asdfads"), ['as', 'df', 'ad', 's_'])
