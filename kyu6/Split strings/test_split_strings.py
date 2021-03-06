from asserts.Asserts import assert_true
import importlib

solution = importlib.import_module('kyu6.Split strings.solution').solution


class TestSolution:
    def test_split_strings(self):
        assert_true(solution('asdfadsf'), ['as', 'df', 'ad', 'sf'])
        assert_true(solution("asdfads"), ['as', 'df', 'ad', 's_'])
