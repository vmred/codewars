import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

Python = importlib.import_module('katas.8kyu.Name your python.solution').Python

cases = [
    Case('Bubba', 'Bubba'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_name_your_python(self, test):
        assert_true(Python(test.test_data).name, test.test_output)
