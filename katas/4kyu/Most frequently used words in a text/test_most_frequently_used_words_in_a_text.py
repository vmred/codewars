import importlib
import pytest
from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.4kyu.Most frequently used words in a text.solution').top_3_words

cases = [
    Case("a a a  b  c c  d d d d  e e e e e", ["e", "d", "a"]),
    Case("  //wont won't won't ", ["won't", "wont"]),
    Case("  '''  ", []),
    Case("  , e   .. ", ["e"]),
    Case(
        """In a village of La Mancha, the name of which I have no desire to call to
        mind, there lived not long since one of those gentlemen that keep a lance
        in the lance-rack, an old buckler, a lean hack, and a greyhound for
        coursing. An olla of rather more beef than mutton, a salad on most
        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
        on Sundays, made away with three-quarters of his income.""",
        ["a", "of", "on"],
    ),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_most_frequently_used_words_in_a_text(self, test):
        assert_true(solution(test.test_data), test.test_output)
