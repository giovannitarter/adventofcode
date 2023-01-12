import unittest

sol = __import__("sol")


def compare_lists(a, b):

    if len(a) != len(b):
        return False

    for x, y in zip(a, b):
        if x != y :
            print(a)
            print(b)
            return False

    return True




class TestAoC(unittest.TestCase):

    def setUp(self):

        with open("test") as fd:
            data = fd.read()
            self.test_data = sol.parse_input(data)

        with open("input") as fd:
            data = fd.read()
            self.input_data = sol.parse_input(data)

    def test_sol01_ex(self):
        self.assertEqual(sol.sol01(self.test_data), 3)
        return

    def test_sol02_ex(self):
        self.assertEqual(sol.sol02(self.test_data), 1623178306)
        return

    def test_sol01_input(self):
        self.assertEqual(sol.sol01(self.input_data), 4426)
        return

    def test_sol02_input(self):
        self.assertEqual(sol.sol02(self.input_data), 8119137886612)
        return


    def compare_sol(self, pos, val):
        data = [0, 10, 11, 12, 13, 14, 15, 16]
        data.insert(pos, val)

        data = [(x, 0) for x in data]
        sdata = sol.shift_sol((val, 0), list(data))
        mdata = sol.mod_sol((val, 0), list(data))
        self.assertTrue(compare_lists(sdata, mdata))
        return


    def test_moves(self):
        self.compare_sol(3, -5)
        self.compare_sol(1, -12)
        self.compare_sol(0, -12)


if __name__ == "__main__":
    unittest.main()

