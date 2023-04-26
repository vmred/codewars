from asserts.asserts import assert_true
import importlib

longest_consec = importlib.import_module('katas.6kyu.Consecutive strings.solution').longest_consec


class TestSolution:
    def test_consecutive_strings(self):
        assert_true(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
        assert_true(
            longest_consec(['wlwsasphmxx', 'owiaxujylentrklctozmymu', 'wpgozvxxiu'], 2),
            'wlwsasphmxxowiaxujylentrklctozmymu',
        )
