import unittest

sol = __import__("sol")



class TestAoC(unittest.TestCase):

    def setUp(self):

        with open("test") as fd:
            data = fd.read()
            self.test_data = sol.parse_input(data)

        with open("input") as fd:
            data = fd.read()
            self.input_data = sol.parse_input(data)

    def test_sol01_ex(self):
        self.assertEqual(sol.sol01(self.test_data), 110)
        return

    def test_sol02_ex(self):
        self.assertEqual(sol.sol02(self.test_data), 20)
        return

    def test_sol01_input(self):
        self.assertEqual(sol.sol01(self.input_data), 4034)
        return

    def test_sol02_input(self):
        self.assertEqual(sol.sol02(self.input_data), 960)
        return


if __name__ == "__main__":
    unittest.main()
