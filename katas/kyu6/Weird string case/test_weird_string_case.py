import importlib

from asserts.asserts import assert_true

to_weird_case = importlib.import_module('katas.kyu6.Weird string case.solution').to_weird_case


class TestSolution:
    def test_weird_string_case(self):
        assert_true(to_weird_case('This'), 'ThIs')
        assert_true(to_weird_case('is'), 'Is')
        assert_true(to_weird_case('This is a test'), 'ThIs Is A TeSt')
