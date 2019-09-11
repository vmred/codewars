from asserts.Asserts import assert_true


class TestSolutions:
    def test_count_sheep(self):
        from kyu8.Count_sheep.solution import count_sheeps
        array1 = [True, True, True, False,
                  True, True, True, True,
                  True, False, True, False,
                  True, False, False, True,
                  True, True, True, True,
                  False, False, True, True]

        assert_true(count_sheeps(array1), 17)
