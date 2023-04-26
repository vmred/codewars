from asserts.asserts import assert_true
import importlib

abbreviate = importlib.import_module('katas.6kyu.Word a10n (abbreviation).solution').abbreviate


class TestSolution:
    def test_word_a10n_abbreviation(self):
        assert_true(abbreviate("elephant-ride"), "e6t-r2e")
        assert_true(abbreviate('elephant-rides are really fun!'), 'e6t-r3s are r4y fun!')
        assert_true(
            abbreviate("sits'monolithic_on. a_sits, sits; on_cat; sat. "), "s2s'm8c_on. a_s2s, s2s; on_cat; sat. "
        )
