import unittest

sol = __import__("sol")



class TestAoC(unittest.TestCase):

    def read_data(self, filename):
        with open(filename) as fd:
            data = fd.read()
            return(sol.parse_input(data))

    def setUp(self):

        with open("input") as fd:
            data = fd.read()
            self.input_data = sol.parse_input(data)

    def test_sol01_ex(self):
        self.assertEqual(sol.sol01(self.read_data("test11")), 4)
        self.assertEqual(sol.sol01(self.read_data("test12")), 8)
        return

    def test_sol02_ex(self):
        self.assertEqual(sol.sol02(self.read_data("test21")), 4)
        self.assertEqual(sol.sol02(self.read_data("test22")), 8)
        self.assertEqual(sol.sol02(self.read_data("test23")), 10)
        return

    def test_sol01_input(self):
        self.assertEqual(sol.sol01(self.input_data), 6649)
        return

    def test_sol02_input(self):
        self.assertEqual(sol.sol02(self.input_data), 601)
        return


if __name__ == "__main__":
    unittest.main()

