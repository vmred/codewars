from asserts.asserts import assert_true
import importlib

List = importlib.import_module('katas.7kyu.Method for counting total occurence of specific digits.solution').List


class TestSolution:
    def test_count_spec_digits(self):
        l = List()

        integers_list = [1, 1, 2, 3, 1, 2, 3, 4]
        digits_list = [1, 3]
        assert_true(l.count_spec_digits(integers_list, digits_list), [(1, 3), (3, 2)])

        integers_list = [-18, -31, 81, -19, 111, -888]
        digits_list = [1, 8, 4]
        assert_true(l.count_spec_digits(integers_list, digits_list), [(1, 7), (8, 5), (4, 0)])
