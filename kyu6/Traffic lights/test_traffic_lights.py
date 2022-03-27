from asserts.asserts import assert_true
import importlib

traffic_lights = importlib.import_module('kyu6.Traffic lights.solution').traffic_lights


class TestSolution:
    def test_traffic_lights(self):
        assert_true(traffic_lights('C...R............G......', 10), ['C...R............G......',
                                                                     '.C..R............G......',
                                                                     '..C.R............G......',
                                                                     '...CR............G......',
                                                                     '...CO............R......',
                                                                     '....C............O......',
                                                                     '....GC...........R......',
                                                                     '....G.C..........R......',
                                                                     '....G..C.........R......',
                                                                     '....G....C.......R......'])
