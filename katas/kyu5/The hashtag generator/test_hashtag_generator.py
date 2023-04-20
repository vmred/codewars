import importlib

from asserts.asserts import assert_true

generate_hashtag = importlib.import_module('katas.kyu5.The hashtag generator.solution').generate_hashtag


class TestSolution:
    def test_hashtag_generator(self):
        assert_true(generate_hashtag(''), False)
        assert_true(generate_hashtag('Do We have A Hashtag')[0], '#')
        assert_true(generate_hashtag('Codewars'), '#Codewars')
        assert_true(generate_hashtag('Codewars      '), '#Codewars')
        assert_true(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice')
        assert_true(generate_hashtag('codewars is nice'), '#CodewarsIsNice')
        assert_true(generate_hashtag('CodeWars is nice'), '#CodewarsIsNice')
        assert_true(generate_hashtag('c i n'), '#CIN')
        assert_true(generate_hashtag('codewars  is  nice'), '#CodewarsIsNice')
        assert_true(generate_hashtag(
            'Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo'
            'oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'),
            False)
