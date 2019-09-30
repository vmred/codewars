from asserts.Asserts import assert_true
import importlib

ordered_count = importlib.import_module('kyu7.Ordered count of characters.solution').ordered_count


class TestSolution:
    def test_ordered_count_of_characters(self):
        assert_true(ordered_count('abracadabra'), [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)])
