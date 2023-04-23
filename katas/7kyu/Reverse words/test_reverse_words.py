from asserts.asserts import assert_true
import importlib

reverse_words = importlib.import_module('katas.7kyu.Reverse words.solution').reverse_words


class TestSolution:
    def test_reverse_words(self):
        assert_true(reverse_words('The quick brown fox jumps over the lazy dog.'),
                           'ehT kciuq nworb xof spmuj revo eht yzal .god')
        assert_true(reverse_words('apple'), 'elppa')
        assert_true(reverse_words('a b c d'), 'a b c d')
        assert_true(reverse_words('double  spaced  words'), 'elbuod  decaps  sdrow')
