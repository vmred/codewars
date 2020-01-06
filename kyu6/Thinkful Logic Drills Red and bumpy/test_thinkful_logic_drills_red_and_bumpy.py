from asserts.Asserts import assert_true
import importlib

color_probability = importlib.import_module('kyu6.Thinkful Logic Drills Red and bumpy.solution').color_probability


class TestSolution:
    def test_thinkful_logic_drills_red_and_bumpy(self):
        assert_true(color_probability('red', 'bumpy'), '0.57')
        assert_true(color_probability('green', 'bumpy'), '0.14')
        assert_true(color_probability('yellow', 'smooth'), '0.33')
