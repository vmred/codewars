import pytest

from asserts.asserts import assert_true
import importlib

traffic_lights = importlib.import_module('katas.6kyu.Traffic lights.solution').traffic_lights


class TestSolution:
    @pytest.mark.xfail
    @pytest.mark.not_competed
    def test_traffic_lights(self):
        assert_true(
            traffic_lights('C...R............G......', 10),
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
        )
