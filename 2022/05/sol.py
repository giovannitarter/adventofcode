#!/usr/bin/python


import sys
import re
import copy


def print_cols(cols):
    for c in sorted(list(cols.keys())):
        print(f"{c} -> {cols[c]}")
    return


def parse_input(text):

    res = None

    tmp = text.split("\n\n")
    stack = tmp[0]
    stack = stack.split("\n")

    cols = {}
    for line in stack[:-1]:
        #print(line)
        i = 1
        for c in range(1, len(line), 4):
            if line[c] != " ":
                s = cols.get(i, [])
                s.append(line[c])
                cols[i] = s

            i += 1

    for c in cols:
        cols[c].reverse()

    inst = tmp[1]
    inst = [re.match(r"move (\d+) from (\d+) to (\d+)", x) for x in inst.split("\n") if x != ""]
    inst = [(int(x[1]), int(x[2]), int(x[3])) for x in inst]

    return (cols, inst)


def exec_inst(cols, nr, fc, tc):

    for j in range(nr):
        tmp = cols[fc].pop()
        cols[tc].append(tmp)

    return cols


def exec_inst2(cols, nr, fc, tc):

    tmp = []
    for j in range(nr):
        tmp.insert(0, cols[fc].pop())
    cols[tc].extend(tmp)
    return cols


def res_str(cols):
    res = [cols[c][-1] for c in sorted(cols.keys())]
    return "".join(res)


def sol(cols_p, inst, fn):

    cols = copy.deepcopy(cols_p)
    for i in inst:
        cols = fn(cols, *i)

    return res_str(cols)


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    COLS, INST = parse_input(TEXT)

    #print_cols(COLS)
    SOL01 = sol(COLS, INST, exec_inst)
    print("sol01: {}".format(SOL01))

    #print_cols(COLS)
    SOL02 = sol(COLS, INST, exec_inst2)
    print("sol02: {}".format(SOL02))
