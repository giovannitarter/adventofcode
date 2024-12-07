"""AOC day X tests"""

import unittest

sol = __import__("sol")


class TestAoC(unittest.TestCase):
    """
    ensures results are right
    """

    def setUp(self):

        with open("test", encoding="utf8") as fd:
            data = fd.read()
            self.test_data = sol.parse_input(data)

        with open("input", encoding="utf8") as fd:
            data = fd.read()
            self.input_data = sol.parse_input(data)

    def test_test01(self):
        """
        test01
        """
        self.assertEqual(sol.sol01(self.test_data), 143)

    def test_test02(self):
        """
        test02
        """
        self.assertEqual(sol.sol02(self.test_data), 123)

    def test_input01(self):
        """
        input01
        """
        self.assertEqual(sol.sol01(self.input_data), 5329)

    def test_input02(self):
        """
        input02
        """
        self.assertEqual(sol.sol02(self.input_data), 5833)


if __name__ == "__main__":
    unittest.main()
