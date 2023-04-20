import importlib

from asserts.asserts import assert_true

bouncingBall = importlib.import_module('katas.kyu6.Bouncing Balls.solution').bouncingBall


class TestSolution:
    def test_bouncing_balls(self):
        assert_true(bouncingBall(3, 0.66, 1.5), 3)
        assert_true(bouncingBall(30, 0.66, 1.5), 15)
