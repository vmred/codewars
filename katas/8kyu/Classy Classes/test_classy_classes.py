import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

Person = importlib.import_module('katas.8kyu.Classy Classes.solution').Person

cases = [
    Case(['Alex', 16], 'Alexs age is 16'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_classy_classes(self, test):
        assert_true(Person(*test.test_data).info, test.test_output)
