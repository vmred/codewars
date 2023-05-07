import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Mix Fruit Juice.solution').mix_fruit

cases = [
    Case(["banana", "mango", "avocado"], 6),
    Case(["melon", "Mango", "kiwi"], 8),
    Case(["watermelon", "cherry", "avocado"], 8),
    Case(["watermelon", "lime", "tomato"], 9),
    Case(["blackBerry", "coconut", "avocado"], 8),
    Case(["waterMelon", "mango"], 8),
    Case(["watermelon", "pEach"], 9),
    Case(["watermelon", "Orange", "grapes"], 6),
    Case(["watermelon"], 9),
    Case(["BlACKbeRrY", "cOcONuT", "avoCaDo"], 8),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_mix_fruit_juice(self, test):
        assert_true(solution(test.test_data), test.test_output)
