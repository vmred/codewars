import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

zero = importlib.import_module('katas.5kyu.Calculating with functions.solution').zero
one = importlib.import_module('katas.5kyu.Calculating with functions.solution').one
two = importlib.import_module('katas.5kyu.Calculating with functions.solution').two
three = importlib.import_module('katas.5kyu.Calculating with functions.solution').three
four = importlib.import_module('katas.5kyu.Calculating with functions.solution').four
five = importlib.import_module('katas.5kyu.Calculating with functions.solution').five
six = importlib.import_module('katas.5kyu.Calculating with functions.solution').six
seven = importlib.import_module('katas.5kyu.Calculating with functions.solution').seven
eight = importlib.import_module('katas.5kyu.Calculating with functions.solution').eight
nine = importlib.import_module('katas.5kyu.Calculating with functions.solution').nine
plus = importlib.import_module('katas.5kyu.Calculating with functions.solution').plus
minus = importlib.import_module('katas.5kyu.Calculating with functions.solution').minus
divided_by = importlib.import_module('katas.5kyu.Calculating with functions.solution').divided_by
times = importlib.import_module('katas.5kyu.Calculating with functions.solution').times

cases = [
    TestCase('seven(times(five()))', 35),
    TestCase('four(plus(nine()))', 13),
    TestCase('eight(minus(three()))', 5),
    TestCase('six(divided_by(two()))', 3),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_calculating_with_functions(self, test):
        assert_true(eval(f'{test.test_data}'), test.test_output)  # pylint: disable=eval-used
