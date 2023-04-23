from asserts.asserts import assert_true
import importlib

solution = importlib.import_module(
    'katas.7kyu.Currying functions multiply all elements in an array.solution').multiply_all


class TestSolution:
    def test_multiply_all_elements_in_array(self):
        assert_true(solution([1, 2, 3])(1), [1, 2, 3])
        assert_true(solution([1, 2, 3])(2), [2, 4, 6])
        assert_true(solution([1, 2, 3])(0), [0, 0, 0])
        assert_true(solution([])(10), [])
