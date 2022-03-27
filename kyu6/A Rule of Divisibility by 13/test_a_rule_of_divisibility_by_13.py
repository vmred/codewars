from asserts.asserts import assert_true
import importlib

thirt = importlib.import_module('kyu6.A Rule of Divisibility by 13.solution').thirt


class TestSolution:
    def test_a_rule_of_divisibility_by_13(self):
        assert_true(thirt(8529), 79)
        assert_true(thirt(1234567), 87)
