from asserts.Asserts import assert_true
import importlib

Ball = importlib.import_module('kyu7.Regular ball super ball.solution').Ball


class TestSolution:
    def test_regular_ball_super_ball(self):
        assert_true(Ball().ball_type, "regular")
        assert_true(Ball("super").ball_type, "super")
