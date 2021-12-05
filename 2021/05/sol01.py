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
    x_span = x2 - x1
    y_span = y2 - y1

    points_nr = 1
    
    dx = 1
    if x_span < 0:
        dx = -1

    dy = 1
    if y_span < 0:
        dy = -1
    
    #print(x_span, y_span)

    if x_span == 0 or y_span == 0:
        for x in range(x1, x2 + dx, dx):
            for y in range(y1, y2 + dy, dy):
                res.append((x,y))

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


    RES01 = INTERSECTIONS
    print("res01 : {}".format(RES01))
