import unittest

sol = __import__("sol")



class TestAoC(unittest.TestCase):

    def setUp(self):

        with open("test1") as fd:
            data = fd.read()
            self.test1_data = sol.parse_input(data)

        with open("test2") as fd:
            data = fd.read()
            self.test2_data = sol.parse_input(data)

        with open("input") as fd:
            data = fd.read()
            self.input_data = sol.parse_input(data)

    def test_sol01_ex(self):
        self.assertEqual(sol.sol01(self.test1_data), 142)
        return

    def test_sol02_ex(self):
        self.assertEqual(sol.sol02(self.test2_data), 281)
        return

    def test_sol01_input(self):
        self.assertEqual(sol.sol01(self.input_data), 56108)
        return

    def test_sol02_input(self):
        self.assertEqual(sol.sol02(self.input_data), 55652)
        return


if __name__ == "__main__":
    unittest.main()

