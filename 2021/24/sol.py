#!/usr/bin/python


import sys
import itertools


def parse_input(text):

    res = []
    lines = [x for x in text.split("\n") if x != ""]

    for l in lines:
        inst = tuple(l.split())
        res.append(inst)

    return res


class ALU:

    def __init__(self, text):

        self.mem = {}
        self.inp_idx = 0
        self.inp = text
        return


    def exec(self, inst, p_op1, p_op2=None):

        if p_op2 is not None:
            if p_op2 in ["w", "x", "y", "z"]:
                op2 = self.mem.get(p_op2, 0)
            else:
                op2 = int(p_op2)

        op1 = self.mem.get(p_op1, 0)

        if inst == "inp":
            val = int(self.inp[self.inp_idx])
            self.inp_idx += 1

        elif inst == "add":
            val = op1 + op2

        elif inst == "mul":
            val = op1 * op2

        elif inst == "div":
            val = op1 // op2

        elif inst == "mod":
            val = op1 % op2

        elif inst == "eql":
            val = int(op1 == op2)

        else:
            print("ERROR!")

        self.mem[p_op1] = val

        return


    def get_res(self, var):
        res = self.mem.get(var, 0)
        return res


def run_program(inst, inp, res_var):

    alu = ALU(inp)

    for idx, c in enumerate(list(inst)):
        alu.exec(*c)

    return alu.get_res(res_var)


def extract_params(inst):

    res = []

    for i in range(0, len(inst), 18):
        a = int(inst[i+4][2])
        b = int(inst[i+5][2])
        c = int(inst[i+15][2])
        res.append([a,b,c])

    return res


#def exec_subunit(a, b, c, inp, z):
#    w = inp
#    x = ((z % 26) + b) != w
#    print(f"x: {x}")
#    res = (z // a * (25 * x + 1)) + (w + c) * x
#    return res
#
#
#def exec_monad(params, model_nr):
#
#    z = 0
#    i = 0
#    for p in params:
#        z = exec_subunit(*p, model_nr[i], z)
#        i += 1
#
#    return z


def find_matching_op(PARAMS):

    stack = []
    matches = []
    for idx, p in enumerate(PARAMS):
        if p[0] == 1:
            stack.append(idx)
        elif p[0] == 26:
            matches.append((stack.pop(), idx))

    return matches


def find_nr(params, matches, digits):

    res = [None] * 14
    for push_idx, pop_idx in matches:

        pair = None
        for pu in digits:
            for po in digits:
                pushed = pu + params[push_idx][2]
                if (po - params[pop_idx][1]) == pushed:
                    pair = pu, po
                    break

            if pair is not None:
                res[push_idx] = pu
                res[pop_idx] = po
                break

    res = "".join([str(r) for r in res])
    return res


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)

    PARAMS = extract_params(DATA)
    MATCHING_OP = find_matching_op(PARAMS)
    MAX = find_nr(PARAMS, MATCHING_OP, range(1, 10, 1))
    MIN = find_nr(PARAMS, MATCHING_OP, range(9, 0, -1))

    SOL01 = MAX
    print(f"sol01: {MAX}")

    print(run_program(DATA, SOL01, "z"))

    SOL02 = MIN
    print(f"sol02: {MIN}")

    print(run_program(DATA, SOL02, "z"))

    sys.exit(0)
