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
        self.assertEqual(sol.sol01(self.test_data), "2=-1=0")
        return

    def test_sol02_ex(self):
        self.assertEqual(sol.sol02(self.test_data), None)
        return

    def test_sol01_input(self):
        self.assertEqual(sol.sol01(self.input_data), "2-0-01==0-1=2212=100")
        return

    def test_sol02_input(self):
        self.assertEqual(sol.sol02(self.input_data), None)
        return

    def test_first_2000(self):
        for i in range(50000):
            snafu = sol.to_snafu(i)
            dec = sol.to_dec(snafu)
            self.assertEqual(i, dec)


if __name__ == "__main__":
    unittest.main()

