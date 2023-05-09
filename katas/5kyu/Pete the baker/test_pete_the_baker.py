import importlib
import pytest
from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.5kyu.Pete the baker.solution').cakes

cases = [
    Case([{"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}], 2),
    Case(
        [
            {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
            {"sugar": 500, "flour": 2000, "milk": 2000},
        ],
        0,
    ),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_pete_the_baker(self, test):
        assert_true(solution(*test.test_data), test.test_output)
