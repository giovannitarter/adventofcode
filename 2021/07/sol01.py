#!/usr/bin/python


import sys
import copy


def parse_input(lines):

    res = None
    pos = lines[0].split(",")
    res = [ int(p) for p in pos ]
    return res


def compute_fuel(positions, start, end):
    line = (end + start) // 2
    res = sum([ abs(p - line) for p in positions ])
    return res


def min_fuel(pos):

    res = None

    min_pos = min(pos)
    max_pos = max(pos)
    min_fuel = None

    while (min_pos + 1 < max_pos):

        print("")
        print("min_pos: {}, max_pos: {}".format(min_pos, max_pos))

        half_pos = (max_pos + min_pos) // 2
        print(("half_pos: {}".format(half_pos)))

        lp = compute_fuel(pos, min_pos, half_pos)
        hp = compute_fuel(pos, half_pos, max_pos)
        print("fuel {} -> {}, {}".format(half_pos, lp, hp))

        if lp < hp:
            max_pos = half_pos
            min_fuel = lp
        else:
            min_pos = half_pos
            min_fuel = hp


    #print("fuel {} -> {}".format(1, compute_fuel(pos, 1)))
    #print("fuel {} -> {}".format(3, compute_fuel(pos, 3)))
    #print("fuel {} -> {}".format(10, compute_fuel(pos, 10)))

    res = min_fuel
    return res


if __name__ == "__main__":

    RES01 = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    LINES = [ x for x in TEXT.split("\n") if x != "" ]
    POS = parse_input(LINES)
    RES01 = min_fuel(POS)





    print("res01 : {}".format(RES01))
