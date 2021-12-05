#!/usr/bin/python


import sys
import copy
import re


def parse_vecs(lines):

    res = []
    for l in lines:
        m = re.match("(\d+),(\d+) -> (\d+),(\d+)", l)
        vec = m.groups()
        vec = list(vec)
        vec = [ int(v) for v in vec ]
        res.append(vec)

    return res


def vec_points(x1, y1, x2, y2):

    res = []

    cx = x1
    cy = y1
    
    while cx != x2  or cy != y2:

        res.append((cx, cy))

        if cx < x2:
            cx = cx + 1
        elif cx > x2:
            cx = cx - 1

        if cy < y2:
            cy = cy + 1
        elif cy > y2:
            cy = cy - 1
    
    res.append((cx, cy))


    return res


if __name__ == "__main__":

    RES01 = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    LINES = [ x for x in TEXT.split("\n") if x != "" ]
    

    
    VECS = parse_vecs(LINES)

    MAP = {}
    for v in VECS:
        POINTS = vec_points(*v)
        print("")
        print(POINTS)
        for p in POINTS:
            LINES_NR = MAP.get(p, 0)
            LINES_NR = LINES_NR + 1
            MAP[p] = LINES_NR

    print(MAP)
    
    INTERSECTIONS = 0
    for P in MAP:
        if MAP[P] > 1:
            INTERSECTIONS = INTERSECTIONS + 1


    RES02 = INTERSECTIONS
    print("")
    print("res02 : {}".format(RES02))
