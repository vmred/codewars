import pytest

from asserts.asserts import assert_true
import importlib

class_name_changer = importlib.import_module('katas.7kyu.Python dynamic classes #1.solution').class_name_changer
MyClass = importlib.import_module('katas.7kyu.Python dynamic classes #1.solution').MyClass


class TestSolution:
    @pytest.mark.xfail(reason='Tests not applicable for running under pytest, kata completed')
    def test_python_dynamic_classes(self):
        assert_true(str(MyClass), "<class '__main__.MyClass'>")

        class_name_changer(MyClass, "UsefulClass")
        assert_true(str(MyClass), "<class '__main__.UsefulClass'>")

        class_name_changer(MyClass, "SecondUsefulClass")
        assert_true(str(MyClass), "<class '__main__.SecondUsefulClass'>")
