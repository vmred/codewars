from asserts.asserts import assert_true
import importlib

next_num = importlib.import_module('katas.kyu6.Next polydivisible number.solution').next_num


class TestSolution:
    def test_next_polydivisible_number(self):
        assert_true(next_num(0), 1)
        assert_true(next_num(10), 12)
        assert_true(next_num(11), 12)
        assert_true(next_num(1234), 1236)
        assert_true(next_num(123220), 123252)
        assert_true(next_num(1234567890), 1236004020)
        assert_true(next_num(8375699373040516261617982), None)
        assert_true(next_num(3608528850368400786036725), None)
