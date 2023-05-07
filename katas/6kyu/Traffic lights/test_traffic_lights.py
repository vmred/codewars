import importlib
import pytest
from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Traffic lights.solution').traffic_lights

cases = [
    Case(
        ['C...R............G......', 10],
        [
            'C...R............G......',
            '.C..R............G......',
            '..C.R............G......',
            '...CR............G......',
            '...CO............R......',
            '....C............O......',
            '....GC...........R......',
            '....G.C..........R......',
            '....G..C.........R......',
            '....G....C.......R......',
        ],
    ),
]


class TestSolution:
    @pytest.mark.xfail
    @pytest.mark.not_competed
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_traffic_lights(self, test):
        assert_true(solution(*test.test_data), test.test_output)
