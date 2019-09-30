from asserts.Asserts import assert_true
import importlib

tidyNumber = importlib.import_module('kyu7.Tidy number.solution').tidyNumber


class TestSolution:
    def test_tidy_number(self):
        assert_true(tidyNumber(102), False)
        assert_true(tidyNumber(9672), False)
        assert_true(tidyNumber(2789), True)
