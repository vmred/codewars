from asserts.Asserts import assert_true
import importlib

next_num = importlib.import_module('kyu6.Next polydivisible number.solution').next_num


class TestSolution:
    def test_next_polydivisible_number(self):
        assert_true(next_num(0), 1)
        assert_true(next_num(10), 12)
        assert_true(next_num(11), 12)
        assert_true(next_num(1234), 1236)
        assert_true(next_num(123220), 123252)
