import pytest

from asserts.asserts import assert_true
import importlib

revrot = importlib.import_module('kyu6.Reverse or rotate.solution').revrot


class TestSolution:
    @pytest.mark.xfail
    @pytest.mark.not_competed
    def test_reverse_or_rotate(self):
        assert_true(revrot("3304991787281570455176064327690480265895", 8), "1994033775182780067155464327690480265895")
