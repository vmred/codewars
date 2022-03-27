import importlib

from asserts.asserts import assert_true

count_smileys = importlib.import_module('kyu6.Count the smiley faces!.solution').count_smileys


class TestSolution:
    def test_count_smiley_faces(self):
        assert_true(count_smileys([]), 0)
        assert_true(count_smileys([':D', ':~)', ';~D', ':)']), 4)
        assert_true(count_smileys([':)', ':(', ':D', ':O', ':;']), 2)
        assert_true(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)
