from asserts.asserts import assert_true
import importlib

vaporcode = importlib.import_module('katas.7kyu.VAPORCODE kata.solution').vaporcode


class TestSolution:
    def test_vaporcode_kata(self):
        assert_true(vaporcode("Lets go to the movies"), "L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S")
        assert_true(
            vaporcode("Why isn't my code working?"), "W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?"
        )
