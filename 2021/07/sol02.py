#!/usr/bin/python


import sys
import copy


def parse_input(lines):

    res = None
    pos = lines[0].split(",")
    res = [ int(p) for p in pos ]
    return res


def sum_series(n):
    return n * (n + 1) // 2


def compute_fuel(positions, start, end):
    half = (end + start) // 2
    res = sum([ sum_series(abs(p - half)) for p in positions ])
    return res


def min_fuel(pos):

    res = None

    min_pos = min(pos)
    max_pos = max(pos)
    min_fuel = None

    while min_pos + 1 < max_pos:

        print("")
        print("min_pos: {}, max_pos: {}".format(min_pos, max_pos))

        half_pos = int((max_pos + min_pos) / 2)
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

    res = min_fuel
    return res


def min_fuel_rec(pos, start, end):

    if start >= end:
        return compute_fuel(pos, start, end)

    else:
        half = (start + end) // 2
        lv = compute_fuel(pos, start, half)
        hv = compute_fuel(pos, half, end)

        if lv > hv:
            return min_fuel_rec(pos, half, end)
        else:
            return min_fuel_rec(pos, start, half)



if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    LINES = [ x for x in TEXT.split("\n") if x != "" ]
    POS = parse_input(LINES)

    #print("fuel {} -> {}".format(2, compute_fuel(pos, 2)))

    #RES = min_fuel(POS)
    RES = min_fuel_rec(POS, min(POS), max(POS))
    print("res : {}".format(RES))
