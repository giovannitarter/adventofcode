#!/usr/bin/python


import sys
import copy


def parse_input(lines):

    res = None
    pos = lines[0].split(",")
    res = [ int(p) for p in pos ]
    return res


def compute_fuel(positions, line):
    res = sum([ abs(p - line) for p in positions ])
    return res


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    LINES = [ x for x in TEXT.split("\n") if x != "" ]
    POS = parse_input(LINES)

    line = sorted(POS)[len(POS) // 2]
    print(line)
    RES = compute_fuel(POS, line)





    print("res : {}".format(RES))
