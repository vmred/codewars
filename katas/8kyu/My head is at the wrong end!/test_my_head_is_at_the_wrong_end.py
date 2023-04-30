import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.8kyu.My head is at the wrong end!.solution').fix_the_meerkat

cases = [
    TestCase(["tail", "body", "head"], ["head", "body", "tail"]),
    TestCase(["bottom", "middle", "top"], ["top", "middle", "bottom"]),
    TestCase(["lower legs", "torso", "upper legs"], ["upper legs", "torso", "lower legs"]),
    TestCase(["ground", "rainbow", "sky"], ["sky", "rainbow", "ground"]),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_my_head_is_at_the_wrong_end(self, test):
        assert_true(solution(test.test_data), test.test_output)
