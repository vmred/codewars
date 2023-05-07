import importlib
import pytest
from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Remove the parentheses.solution').remove_parentheses

cases = [
    Case("example(unwanted thing)example", "exampleexample"),
    Case("example (unwanted thing) example", "example  example"),
    Case("(first group) (second group)", " "),
    Case("(first group) (second group) (third group)", "  "),
    Case('a(b(c))', 'a'),
    Case('a()b', 'ab'),
    Case(
        'ZkYEU(TRKi(foc yH(NCfGZadCZCQBGe)zPe)f(uVzc NQouaAnl sDH)qEXMalfsq(DrN ) ) JujCiQLXmItT MNrtctBBB(Qv(masDq()TSMOyalhRFHMRWlrFXwj)uCxVlB(dMZvNqQTFGFzdCUFUIOQCMsZh)tplXyi)() Q(RJQuNn  qtkNSHmOSolYTpRd)ROMDTYCCq QUYxHAj(vHZFQYBMwE(BjHgvUrDGSn)AZ H(VMN(mzAe T fNuxE)ot a REt()dF) GXb)nGQiooD(XTcVVNhMIQIQOdBD )(P AH)zedcAJR(CyvjJMJOqaN)V(HJ zhiUAAPWxGTxqO)tIqWIameI OcK zgerm',
        'ZkYEU JujCiQLXmItT MNrtctBBB QROMDTYCCq QUYxHAjnGQiooDzedcAJRVtIqWIameI OcK zgerm',
    ),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_remove_the_parentheses(self, test):
        assert_true(solution(test.test_data), test.test_output)
