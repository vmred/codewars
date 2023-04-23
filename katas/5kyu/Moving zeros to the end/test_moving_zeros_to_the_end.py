import importlib

from asserts.asserts import assert_true

move_zeros = importlib.import_module('katas.5kyu.Moving zeros to the end.solution').move_zeros


class TestSolution:
    def test_moving_zeros_to_the_end(self):
        # assert_true(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]), [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
        # assert_true(move_zeros([9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
        #             [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        assert_true(move_zeros([0, 1, None, 2, False, 1, 0]), [1, None, 2, False, 1, 0, 0])
