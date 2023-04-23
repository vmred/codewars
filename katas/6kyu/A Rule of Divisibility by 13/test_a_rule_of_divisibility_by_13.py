from asserts.asserts import assert_true
import importlib

solution = importlib.import_module('katas.6kyu.A Rule of Divisibility by 13.solution').thirt


class TestSolution:
    def test_a_rule_of_divisibility_by_13(self):
        assert_true(solution(8529), 79)
        assert_true(solution(1234567), 87)
