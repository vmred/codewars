from asserts.asserts import assert_true
import importlib

openOrSenior = importlib.import_module('kyu7.Categorize new member.solution').openOrSenior


class TestSolution:
    def test_categorize_new_member(self):
        assert_true(openOrSenior([[45, 12], [55, 21], [19, -2], [104, 20]]),
                    ['Open', 'Senior', 'Open', 'Senior'])
        assert_true(openOrSenior([[16, 23], [73, 1], [56, 20], [1, -1]]), ['Open', 'Open', 'Senior', 'Open'])
