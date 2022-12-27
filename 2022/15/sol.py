#!/usr/bin/python


import sys
import copy
import re

ROW = {
    14: 10,
    38: 2000000,
    }


def parse_input(text):

    lines = [x for x in text.split("\n") if x != ""]
    res = [
            tuple(map(int,
                re.match(
                r"Sensor at x=(\-*\d+), y=(\-*\d+): closest beacon is at x=(\-*\d+), y=(\-*\d+)",
                l
                ).group(1, 2, 3, 4))) for l in lines
        ]

    row = ROW[len(res)]
    return row, res


def manhattan(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)


def sol01(data):

    row, data = data
    res = set()
    for sx, sy, bx, by in data:

        manh = manhattan(sx, sy, bx, by)
        #print(manh)
        sen_row = abs(sy - row)
        if sen_row < manh:
            start_x = sx - (manh - sen_row)
            end_x = sx + (manh - sen_row)
            res.update(range(start_x, end_x))

            #print(f"({start_x}, {row}) -> ({end_x}, {row})")

            #res += end_x - start_x
    res = len(res)
    return res


def calc_ranges(data):

    res = {}
    for sx, sy, bx, by in data:
        res[(sx, sy)] = manhattan(sx, sy, bx, by)

    return res


def find_sensor(x, y, ranges):

    res = None, None

    for r in ranges:
        sx, sy = r
        m = manhattan(sx, sy, x, y)
        if m <= ranges[r]:
            res = r, ranges[r]
            break

    return res


def sol02(data):

    max_coord, data = data
    max_coord = max_coord * 2
    ranges = calc_ranges(data)
    res = None

        #sen_row = abs(sy - row)
        #if sen_row < manh:
        #    start_x = sx - (manh - sen_row)
        #    end_x = sx + (manh - sen_row)

    for y in range(0, max_coord):
        x = 0
        while x < max_coord:
            s, rang = find_sensor(x, y, ranges)
            if s is None:
                res = (x, y)
                break
            else:
                sen_row = abs(s[1] - y)
                x = s[0] + (rang - sen_row) + 1

    res = res[0] * 4000000 + res[1]

    return res


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)
    print(f"DATA:\n{DATA}\n")

    SOL01 = sol01(DATA)
    print("SOL01: {}".format(SOL01))

    SOL02 = sol02(DATA)
    print("SOL02: {}".format(SOL02))

