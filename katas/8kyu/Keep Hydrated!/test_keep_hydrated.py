from asserts.asserts import assert_true
import importlib

litres = importlib.import_module('katas.8kyu.Keep Hydrated!.solution').litres


class TestSolution:
    def test_keep_hydrated(self):
        assert_true(litres(2), 1)
        assert_true(litres(1.4), 0)
        assert_true(litres(12.3), 6)
        assert_true(litres(0.82), 0)
        assert_true(litres(11.8), 5)
        assert_true(litres(1787), 893)
        assert_true(litres(0), 0)
