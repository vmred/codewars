from asserts.asserts import assert_true
import importlib

solution = importlib.import_module('katas.6kyu.Break camelCase.solution').solution


class TestSolution:
    def test_break_camelcase(self):
        assert_true(solution("helloWorld"), "hello World")
        assert_true(solution("camelCase"), "camel Case")
        assert_true(solution("breakCamelCase"), "break Camel Case")
