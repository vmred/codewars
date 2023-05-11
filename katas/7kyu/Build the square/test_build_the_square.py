import importlib
from asserts.asserts import assert_true

solution = importlib.import_module('katas.7kyu.Build the square.solution').generate_shape


class TestSolution:
    def test_build_the_square(self):
        assert_true(solution(3), '+++\n+++\n+++')
        assert_true(solution(8), '++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++')
