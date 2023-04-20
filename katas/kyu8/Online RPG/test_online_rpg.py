from asserts.asserts import assert_true
import importlib

playerRankUp = importlib.import_module('katas.kyu8.Online RPG.solution').playerRankUp


class TestSolution:
    def test_online_rpg(self):
        assert_true(playerRankUp(64), False)
        assert_true(playerRankUp(180),
                    'Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up.')
