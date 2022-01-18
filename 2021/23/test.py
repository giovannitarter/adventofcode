import unittest

sol = __import__("sol")



class TestDay23(unittest.TestCase):


    def test_organized_2rows(self):

        data = (
"""
#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #########
"""
                )

        data = sol.parse_input(data)
        self.assertTrue(sol.is_organized(data))
        return


    def test_organized_4rows(self):

        data = (
"""
#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########
"""
                )

        data = sol.parse_input(data)
        self.assertTrue(sol.is_organized(data))
        return


    def test_moves_2rows(self):

        data = (
"""
#############
#.B.........#
###.#C#B#D###
  #A#D#C#A#
  #########
"""
                )

        data = sol.parse_input(data)
        moves = sol.all_moves(data)
        self.assertEqual(len(moves), 15)
        return


    def test_find_path(self):
        data = (
"""
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
"""
                )

        data = sol.parse_input(data)
        ordered, res = sol.find_best_path(data)
        self.assertEqual(res, 12521)
        return





if __name__ == "__main__":
    unittest.main()

