import pytest
from asserts.asserts import assert_true
import importlib
from asserts.testcase import TestCase

solution = importlib.import_module('katas.6kyu.Remove the parentheses.solution').remove_parentheses

cases = [
    TestCase("example(unwanted thing)example", "exampleexample"),
    TestCase("example (unwanted thing) example", "example  example"),
    TestCase("(first group) (second group)", " "),
    TestCase("(first group) (second group) (third group)", "  "),
    TestCase('a(b(c))', 'a'),
    TestCase('a()b', 'ab'),
    TestCase(
        'ZkYEU(TRKi(foc yH(NCfGZadCZCQBGe)zPe)f(uVzc NQouaAnl sDH)qEXMalfsq(DrN ) ) JujCiQLXmItT MNrtctBBB(Qv(masDq()TSMOyalhRFHMRWlrFXwj)uCxVlB(dMZvNqQTFGFzdCUFUIOQCMsZh)tplXyi)() Q(RJQuNn  qtkNSHmOSolYTpRd)ROMDTYCCq QUYxHAj(vHZFQYBMwE(BjHgvUrDGSn)AZ H(VMN(mzAe T fNuxE)ot a REt()dF) GXb)nGQiooD(XTcVVNhMIQIQOdBD )(P AH)zedcAJR(CyvjJMJOqaN)V(HJ zhiUAAPWxGTxqO)tIqWIameI OcK zgerm',
        'ZkYEU JujCiQLXmItT MNrtctBBB QROMDTYCCq QUYxHAjnGQiooDzedcAJRVtIqWIameI OcK zgerm'
    )
]


class TestSolution:

    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_remove_the_parentheses(self, test):
        assert_true(solution(test.test_data), test.test_output)
