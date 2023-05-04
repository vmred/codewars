import importlib
from asserts.asserts import assert_true

tidyNumber = importlib.import_module('katas.7kyu.Tidy number.solution').tidyNumber


class TestSolution:
    def test_tidy_number(self):
        assert_true(tidyNumber(102), False)
        assert_true(tidyNumber(9672), False)
        assert_true(tidyNumber(2789), True)
