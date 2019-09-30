from asserts.Asserts import assert_true
import importlib

jumping_number = importlib.import_module('kyu7.Jumping number.solution').jumping_number


class TestSolution:
    def test_jumping_number(self):
        assert_true(jumping_number(79), "Not!!")
        assert_true(jumping_number(98), "Jumping!!")
        assert_true(jumping_number(98789876), 'Jumping!!')
