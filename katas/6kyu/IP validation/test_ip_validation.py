import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.IP validation.solution').is_valid_IP

cases = [
    Case('12.255.56.1', True),
    Case('', False),
    Case('abc.def.ghi.jkl', False),
    Case('12.34.56 .1', False),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_ip_validation(self, test):
        assert_true(solution(test.test_data), test.test_output)
