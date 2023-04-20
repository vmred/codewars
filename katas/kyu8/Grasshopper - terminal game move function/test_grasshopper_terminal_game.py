from asserts.asserts import assert_true
import importlib

move = importlib.import_module('katas.kyu8.Grasshopper - terminal game move function.solution').move


class TestSolution:
    def test_grasshopper_terminal_game(self):
        assert_true(move(0, 4), 8)
        assert_true(move(3, 6), 15)
        assert_true(move(2, 5), 12)
