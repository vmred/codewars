from asserts.asserts import assert_true
import importlib

strong_num = importlib.import_module('katas.7kyu.STRONG strong number.solution').strong_num


class TestSolution:
    def test_strong_strong_number(self):
        assert_true(strong_num(1), 'STRONG!!!!')
        assert_true(strong_num(145), 'STRONG!!!!')
        assert_true(strong_num(7), 'Not Strong !!')
        assert_true(strong_num(185), "Not Strong !!")
