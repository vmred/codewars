from asserts.Asserts import assert_true
import importlib

check_coupon = importlib.import_module('kyu7.The coupon code.solution').check_coupon


class TestSolution:
    def test_coupon_code(self):
        assert_true(check_coupon('123', '123', 'September 5, 2014', 'October 1, 2014'), True)
        assert_true(check_coupon('123a', '123', 'September 5, 2014', 'October 1, 2014'), False)
        assert_true(check_coupon(0, False, 'September 5, 2014', 'September 25, 2014'), False)
