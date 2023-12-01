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

    #def test_sol01_ex(self):
    #    self.assertEqual(sol.sol01(self.test_data), 33)
    #    return

    #def test_sol02_ex(self):
    #    self.assertEqual(sol.sol02(self.test_data), 56)
    #    return

    #def test_sol01_input(self):
    #    self.assertEqual(sol.sol01(self.input_data), 1413)
    #    return

    #def test_sol02_input(self):
    #    self.assertEqual(sol.sol02(self.input_data), None)
    #    return

    def test_neighbor(self):

        #min 1
        self.assertIn(
            (5, 0, (1, 0, 0, 0), (2, 0, 0, 0)),
            sol.get_neighs(
                (0, 0, 0, 0),
                (1, 0, 0, 0),
                self.test_data[1],
                (0, 0, 0, 0)
                )
            )

        #min 8
        self.assertIn(
            (3, 2, (2, 4, 0, 0), (1, 3, 1, 0)),
            sol.get_neighs(
                (2, 9, 0, 0),
                (1, 3, 0, 0),
                self.test_data[1],
                (0, 0, 0, 0)
                )
            )


        #min 10
        self.assertIn(
            (1, 2, (2, 4, 0, 0), (1, 3, 1, 0)),
            sol.get_neighs(
                (4, 15, 0, 0),
                (1, 3, 0, 0),
                self.test_data[1],
                (0, 0, 0, 0)
                )
            )


        #min 20
        self.assertIn(
            (1, 3, (3, 29, 2, 3), (1, 4, 2, 2)),
            sol.get_neighs(
                (4, 25, 7, 2),
                (1, 4, 2, 1),
                self.test_data[1],
                (0, 0, 0, 0)
                )
            )

        return



if __name__ == "__main__":
    unittest.main()

