import importlib

from asserts.asserts import assert_true

solution = importlib.import_module('katas.4kyu.Strip comments.solution').solution


class TestSolution:
    def test_solution(self):
        assert_true(
            solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]),
            "apples, pears\ngrapes\nbananas",
        )
        # assert_true(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")
