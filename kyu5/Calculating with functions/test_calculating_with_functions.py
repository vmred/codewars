import importlib

from asserts.asserts import assert_true

zero = importlib.import_module('kyu5.Calculating with functions.solution').zero
one = importlib.import_module('kyu5.Calculating with functions.solution').one
two = importlib.import_module('kyu5.Calculating with functions.solution').two
three = importlib.import_module('kyu5.Calculating with functions.solution').three
four = importlib.import_module('kyu5.Calculating with functions.solution').four
five = importlib.import_module('kyu5.Calculating with functions.solution').five
six = importlib.import_module('kyu5.Calculating with functions.solution').six
seven = importlib.import_module('kyu5.Calculating with functions.solution').seven
eight = importlib.import_module('kyu5.Calculating with functions.solution').eight
nine = importlib.import_module('kyu5.Calculating with functions.solution').nine
plus = importlib.import_module('kyu5.Calculating with functions.solution').plus
minus = importlib.import_module('kyu5.Calculating with functions.solution').minus
divided_by = importlib.import_module('kyu5.Calculating with functions.solution').divided_by
times = importlib.import_module('kyu5.Calculating with functions.solution').times


class TestSolution:
    def test_calculating_with_functions(self):
        assert_true(seven(times(five())), 35)
        assert_true(four(plus(nine())), 13)
        assert_true(eight(minus(three())), 5)
        assert_true(six(divided_by(two())), 3)
