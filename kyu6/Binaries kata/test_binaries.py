import importlib

from asserts.Asserts import assert_true

code = importlib.import_module('kyu6.Binaries kata.solution').code
decode = importlib.import_module('kyu6.Binaries kata.solution').decode


class TestSolution:

    def testing_code(self, s, expected):
        actual = code(s)
        assert_true(actual, expected)

    def testing_decode(self, s, expected):
        actual = decode(s)
        assert_true(actual, expected)

    def test_code(self):
        self.testing_code("62", "0011100110")
        self.testing_code("55337700", "001101001101011101110011110011111010")
        self.testing_code("1119441933000055", "1111110001100100110000110011000110010111011110101010001101001101")
        self.testing_code("69", "00111000011001")
        self.testing_code("86", "00011000001110")
        self.testing_code("07", "10001111")

    def test_decode(self):
        self.testing_decode("10001111", "07")
        # self.testing_decode(
        #     "001100001100001100001110001110001110011101110111001110001110001110001111001111001111001100001100001100",
        #     "444666333666777444")
        # self.testing_decode("01110111110001100100011000000110000011110011110111011100110000110001100110",
        #                     "33198877334422")
        # self.testing_decode(
        #     "0011010011010011011010101111110011000011000011000011100011100011100011100011100011100001100100011001000110011100011001001111001111001111001111001111001111",
        #     "55500011144466666699919777777")
        # self.testing_decode(
        #     "01110111011111000110010011110011110011110011110011110011110111011101110110011001100110011001101111111010101100011001000110000001100000011000",
        #     "3331977777733322222211100019888")
