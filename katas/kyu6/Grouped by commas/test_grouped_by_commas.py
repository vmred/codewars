from asserts.asserts import assert_true
import importlib

group_by_commas = importlib.import_module('katas.kyu6.Grouped by commas.solution').group_by_commas


class TestSolution:
    def test_grouped_by_commas(self):
        assert_true(group_by_commas(35235235), '35,235,235')
        assert_true(group_by_commas(1000000), '1,000,000')
