import unittest

sol = __import__("sol")



class TestAoC(unittest.TestCase):

    def test0(self):

        inp = "5"
        inst = (
"""
inp x
mul x -1
"""
        )

        alu = sol.ALU(inp)
        cmds = sol.parse_input(inst)
        for c in cmds:
            alu.exec(*c)

        res = alu.get_res("x")
        self.assertEqual(res, -5)
        return


    def test1(self):

        inp = ["4", "12"]
        inst = (
"""
inp z
inp x
mul z 3
eql z x
"""
        )

        alu = sol.ALU(inp)
        cmds = sol.parse_input(inst)
        for c in cmds:
            alu.exec(*c)

        res = alu.get_res("z")
        self.assertEqual(res, 1)
        return


    def test2(self):

        inp = ["4", "11"]
        inst = (
"""
inp z
inp x
mul z 3
eql z x
"""
        )

        alu = sol.ALU(inp)
        cmds = sol.parse_input(inst)
        for c in cmds:
            alu.exec(*c)

        res = alu.get_res("z")
        self.assertEqual(res, 0)
        return


    def test3(self):

        for i in range(0, 16):
            inp = [i]

            inst = (
"""
inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2
"""
            )

            alu = sol.ALU(inp)
            cmds = sol.parse_input(inst)
            for c in cmds:
                alu.exec(*c)

            res = "".join([str(alu.get_res(x)) for x in ["w", "x", "y", "z"]])
            res = int(res, 2)
            self.assertEqual(res, i)
        return


    def test4(self):

        model_nr = "13579246899999"

        fd = open("input", "r")
        inst = fd.read()
        fd.close()

        cmds = sol.parse_input(inst)
        res = sol.run_program(cmds, list(model_nr), "z")

        self.assertNotEqual(res, 0)
        return


if __name__ == "__main__":
    unittest.main()

