from asserts.asserts import assert_true
import importlib

flatten = importlib.import_module('katas.kyu5.flatten() kata.solution').flatten


class TestSolution:
    def test_flatten_kata(self):
        assert_true(flatten([[1], [[8]]]), [1, 8])
        assert_true(flatten([[1, 2, 3]]), [1, 2, 3])
        assert_true(flatten(), [])
        assert_true(flatten(1, 2, 3), [1, 2, 3])
        assert_true(flatten([1, 2], [3, 4, 5], [6, [7], [[8]]]), [1, 2, 3, 4, 5, 6, 7, 8])
        assert_true(flatten(1, 2, ['9', [], []], None), [1, 2, '9', None])
        assert_true(flatten(['hello', 2, ['text', [4, 5]]], [[]], '[list]'), ['hello', 2, 'text', 4, 5, '[list]'])
