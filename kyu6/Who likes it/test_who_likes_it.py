from asserts.Asserts import assert_true
import importlib

likes = importlib.import_module('kyu6.Who likes it.solution').likes


class TestSolution:
    def test_who_likes_it(self):
        assert_true(likes([]), 'no one likes this')
        assert_true(likes(['Peter']), 'Peter likes this')
        assert_true(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
        assert_true(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
        assert_true(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')
