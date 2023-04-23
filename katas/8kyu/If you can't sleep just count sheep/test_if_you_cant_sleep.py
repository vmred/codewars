import importlib

from asserts.asserts import assert_true

count_sheep = importlib.import_module('katas.8kyu.If you can\'t sleep just count sheep.solution').count_sheep


class TestSolution:
    def test_if_you_cant_sleep(self):
        assert_true(count_sheep(1), '1 sheep...')
        assert_true(count_sheep(2), "1 sheep...2 sheep...")
