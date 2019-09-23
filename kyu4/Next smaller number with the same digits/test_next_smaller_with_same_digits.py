import importlib

from asserts.Asserts import assert_true

next_smaller = importlib.import_module('kyu4.Next smaller number with the same digits.solution').next_smaller


class TestSolution:
    def test_nex_smaller_with_same_digits(self):
        assert_true(next_smaller(1027), -1)
        assert_true(next_smaller(907), 790)
        assert_true(next_smaller(531), 513)
        assert_true(next_smaller(135), -1)
        assert_true(next_smaller(2071), 2017)
        assert_true(next_smaller(414), 144)
        assert_true(next_smaller(123456798), 123456789)
        assert_true(next_smaller(123456789), -1)
        assert_true(next_smaller(1234567908), 1234567890)
