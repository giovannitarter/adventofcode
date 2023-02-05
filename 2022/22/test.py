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
        self.assertEqual(sol.sol01(self.test_data), 6032)
        return

    #def test_sol02_ex(self):
    #    self.assertEqual(sol.sol02(self.test_data), 5031)
    #    return

    def test_sol01_input(self):
        self.assertEqual(sol.sol01(self.input_data), 106094)
        return

    #def test_sol02_input(self):
    #    self.assertEqual(sol.sol02(self.input_data), None)
    #    return

    def test_progression(self):

        #1 -> 6
        self.assertEqual(sol.cube_progression(8, 0, 0, 7, self.test_data), (12, 11, 2))
        self.assertEqual(sol.cube_progression(8, 1, 0, 7, self.test_data), (12, 10, 2))

        #6 -> 1
        self.assertEqual(sol.cube_progression(12, 11, 0, 7, self.test_data), (8, 0, 2))
        self.assertEqual(sol.cube_progression(12, 10, 0, 7, self.test_data), (8, 1, 2))

        #1 -> 3
        self.assertEqual(sol.cube_progression(11, 0, 2, 7, self.test_data), (4, 7, 1))
        self.assertEqual(sol.cube_progression(11, 1, 2, 7, self.test_data), (5, 7, 1))

        #3 -> 1
        self.assertEqual(sol.cube_progression(4, 7, 3, 7, self.test_data), (11, 0, 0))
        self.assertEqual(sol.cube_progression(5, 7, 3, 7, self.test_data), (11, 1, 0))

        #1 -> 2
        self.assertEqual(sol.cube_progression(8, 3, 3, 7, self.test_data), (3, 7, 1))
        self.assertEqual(sol.cube_progression(11, 3, 3, 7, self.test_data), (0, 7, 1))

        #2 -> 1
        self.assertEqual(sol.cube_progression(3, 7, 3, 7, self.test_data), (8, 3, 1))
        self.assertEqual(sol.cube_progression(0, 7, 3, 7, self.test_data), (11, 3, 1))

        #2 -> 5
        self.assertEqual(sol.cube_progression(0, 4, 1, 7, self.test_data), (11, 8, 3))
        self.assertEqual(sol.cube_progression(3, 4, 1, 7, self.test_data), (8, 8, 3))

        #5 -> 2
        self.assertEqual(sol.cube_progression(8, 8, 1, 7, self.test_data), (3, 4, 3))
        self.assertEqual(sol.cube_progression(11, 8, 1, 7, self.test_data), (0, 4, 3))

        #2 -> 6
        self.assertEqual(sol.cube_progression(3, 4, 2, 7, self.test_data), (15, 8, 3))
        self.assertEqual(sol.cube_progression(3, 7, 2, 7, self.test_data), (12, 8, 3))

        #6 -> 2
        self.assertEqual(sol.cube_progression(12, 8, 1, 7, self.test_data), (3, 7, 0))
        self.assertEqual(sol.cube_progression(15, 8, 1, 7, self.test_data), (3, 4, 0))

        #3 -> 5
        self.assertEqual(sol.cube_progression(4, 4, 1, 7, self.test_data), (11, 11, 0))
        self.assertEqual(sol.cube_progression(7, 4, 1, 7, self.test_data), (11, 8, 0))

        #5 -> 3
        self.assertEqual(sol.cube_progression(11, 8, 2, 7, self.test_data), (7, 4, 3))
        self.assertEqual(sol.cube_progression(11, 11, 2, 7, self.test_data), (4, 4, 3))

        #4 -> 6
        self.assertEqual(sol.cube_progression(8, 4, 0, 7, self.test_data), (15, 11, 1))
        self.assertEqual(sol.cube_progression(8, 7, 0, 7, self.test_data), (12, 11, 1))

        #6 -> 4
        self.assertEqual(sol.cube_progression(15, 11, 3, 7, self.test_data), (8, 4, 2))
        self.assertEqual(sol.cube_progression(12, 11, 3, 7, self.test_data), (8, 7, 2))


        return


if __name__ == "__main__":
    unittest.main()

