import importlib
from decimal import Decimal
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Round and Round.solution').round_by_2_decimal_places

cases = [
    Case(Decimal('2'), Decimal('2')),
    Case(Decimal('7.477'), Decimal('7.48')),
    Case(Decimal('-4.999'), Decimal('-5')),
    Case(Decimal('18.123'), Decimal('18.12')),
    Case(Decimal('0'), Decimal('0')),
    Case(Decimal('1.455'), Decimal('1.46')),
    Case(Decimal('-1.455'), Decimal('-1.46')),
    Case(Decimal('1.055'), Decimal('1.06')),
    Case(Decimal('-1.055'), Decimal('-1.06')),
    Case(Decimal('16.765'), Decimal('16.77')),
    Case(Decimal('-16.765'), Decimal('-16.77')),
    Case(Decimal('1.025'), Decimal('1.03')),
    Case(Decimal('-1.025'), Decimal('-1.03')),
    Case(Decimal('16.355'), Decimal('16.36')),
    Case(Decimal('-16.345'), Decimal('-16.35')),
    Case(Decimal('-1.1949999999999999999999999999'), Decimal('-1.19')),
    Case(Decimal('-1.1950000000000000000000000001'), Decimal('-1.2')),
    Case(Decimal('1.1949999999999999999999999999'), Decimal('1.19')),
    Case(Decimal('1.1950000000000000000000000001'), Decimal('1.2')),
    Case(Decimal('-1.1849999999999999999999999999'), Decimal('-1.18')),
    Case(Decimal('-1.1850000000000000000000000001'), Decimal('-1.19')),
    Case(Decimal('1.1849999999999999999999999999'), Decimal('1.18')),
    Case(Decimal('1.1850000000000000000000000001'), Decimal('1.19')),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_round_and_round(self, test):
        assert_true(solution(test.test_data), test.test_output)
