import importlib
import pytest
from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.5kyu.Perimeter of squares in a rectangle.solution').perimeter

cases = [
    Case(
        500,
        2362425027542282167538999091770205712168371625660854753765546783141099308400948230006358531927265833165504
    ),
    Case(100, 6002082144827584333104),
    Case(30, 14098308),
    Case(5, 80),
]


class TestSolution:

    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_perimeter_of_squares_in_a_rectangle(self, test):
        assert_true(solution(test.test_data), test.test_output)
