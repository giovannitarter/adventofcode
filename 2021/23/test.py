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


    def test_moves_2rows_to_hallway1(self):

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
        moves = sol.all_single_amphipod_moves(data, (3,2))
        self.assertEqual(len(moves), 7)
        return


    def test_moves_2rows_to_hallway2(self):

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
        moves = sol.all_single_amphipod_moves(data, (2,1))
        self.assertEqual(len(moves), 0)
        return


    def test_moves_2rows_to_hallway3(self):

        data = (
"""
#############
#...B.......#
###.#C#B#D###
  #A#D#C#A#
  #########
"""
                )

        data = sol.parse_input(data)
        moves = sol.all_single_amphipod_moves(data, (4, 1))
        self.assertEqual(len(moves), 0)
        return


    def test_moves_2rows_to_hallway4(self):

        data = (
"""
#############
#...A.......#
###.#C#B#D###
  #A#D#C#A#
  #########
"""
                )

        data = sol.parse_input(data)
        moves = sol.all_single_amphipod_moves(data, (4, 1))
        self.assertEqual(len(moves), 1)
        return


    def test_moves_2rows_to_rooms1(self):

        data = (
"""
#############
#...A.A.....#
###.#C#B#D###
  #.#D#C#B#
  #########
"""
                )

        data = sol.parse_input(data)
        moves = sol.all_single_amphipod_moves(data, (4,1))
        self.assertEqual(len(moves), 1)
        return


    def test_moves_2rows_to_rooms2(self):

        data = (
"""
#############
#...B...A...#
###.#C#B#D###
  #A#D#C#B#
  #########
"""
                )

        data = sol.parse_input(data)
        moves = sol.all_single_amphipod_moves(data, (5,3))
        self.assertEqual(len(moves), 0)
        return


    def test_moves_4rows_to_room(self):

        data = (
"""
#############
#A......B..B#
###B#.#.#D###
  #D#.#C#A#
  #D#B#C#C#
  #A#D#C#A#
  #########
"""
        )

        data = sol.parse_input(data)
        moves = sol.all_single_amphipod_moves(data, (8,1))
        self.assertEqual(len(moves), 0)
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


    def test_find_path2(self):
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
        data = sol.add_folded(data)
        ordered, res = sol.find_best_path(data)
        self.assertEqual(res, 44169)
        return


if __name__ == "__main__":
    unittest.main()

