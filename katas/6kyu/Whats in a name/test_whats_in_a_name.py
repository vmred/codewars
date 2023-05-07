import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Whats in a name.solution').name_in_str

cases = [
    Case(["Across the rivers", "chris"], True),
    Case(["A crew that boards the ship", "chris"], False),
    Case(["Next to a lake", "chris"], False),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_whats_in_a_name(self, test):
        assert_true(solution(*test.test_data), test.test_output)
