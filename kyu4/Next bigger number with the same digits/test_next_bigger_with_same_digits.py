import importlib

from asserts.asserts import assert_true

next_bigger = importlib.import_module('kyu4.Next bigger number with the same digits.solution').next_bigger


class TestSolution:
    def test_nex_smaller_with_same_digits(self):
        assert_true(next_bigger(12), 21)
        assert_true(next_bigger(513), 531)
        assert_true(next_bigger(2017), 2071)
        assert_true(next_bigger(414), 441)
        assert_true(next_bigger(144), 414)
