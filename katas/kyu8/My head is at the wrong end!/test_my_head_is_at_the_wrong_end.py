from asserts.asserts import assert_true
import importlib

fix_the_meerkat = importlib.import_module('katas.kyu8.My head is at the wrong end!.solution').fix_the_meerkat


class TestSolution:
    def test_my_head_is_at_the_wrong_end(self):
        assert_true(fix_the_meerkat(["tail", "body", "head"]), ["head", "body", "tail"])
        assert_true(fix_the_meerkat(["tails", "body", "heads"]), ["heads", "body", "tails"])
        assert_true(fix_the_meerkat(["bottom", "middle", "top"]), ["top", "middle", "bottom"])
        assert_true(fix_the_meerkat(["lower legs", "torso", "upper legs"]),
                           ["upper legs", "torso", "lower legs"])
        assert_true(fix_the_meerkat(["ground", "rainbow", "sky"]), ["sky", "rainbow", "ground"])
