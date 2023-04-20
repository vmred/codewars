from asserts.asserts import assert_true
import importlib

snail = importlib.import_module('katas.kyu4.Snail kata.solution').snail


class TestSolution:
    def test_snail_kata(self):
        array = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        assert_true(snail(array), expected)

        array = [[1, 2, 3],
                 [8, 9, 4],
                 [7, 6, 5]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert_true(snail(array), expected)
