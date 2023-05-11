import importlib
from asserts.asserts import assert_true

solution = importlib.import_module('katas.7kyu.Categorize new member.solution').open_or_senior


class TestSolution:
    def test_categorize_new_member(self):
        assert_true(solution([[45, 12], [55, 21], [19, -2], [104, 20]]), ['Open', 'Senior', 'Open', 'Senior'])
        assert_true(solution([[16, 23], [73, 1], [56, 20], [1, -1]]), ['Open', 'Open', 'Senior', 'Open'])
