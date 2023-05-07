import importlib
import pytest
from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.4kyu.Counting Change Combinations.solution').count_change

cases = [
    Case([4, [1, 2]], 3),
    Case([10, [5, 2, 3]], 4),
    Case([1116, [2, 212, 494, 73, 335]], 61),
    Case([886, [245, 30, 356, 97, 158]], 3),
    Case([1474, [313, 395, 144, 354, 268]], 2),
    Case([4608, [200, 352, 412, 188]], 26),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_counting_change_combinations(self, test):
        assert_true(solution(*test.test_data), test.test_output)
