#!/usr/bin/python


import sys
import copy
import heapq
from itertools import combinations


def parse_input(text):

    res = [list(x) for x in text.split("\n") if x != ""]

    return res


def print_data(data):
    print("\n".join(["".join(d) for d in data]))


def row_map(data, warp):
    r_map = {}
    cnt = 0
    for y, row in enumerate(data):
        if all([c == "." for c in row]):
            cnt += (warp-1)
        r_map[y] = cnt
        cnt += 1
    return r_map


def extend(data, warp):
    return  row_map(zip(*data), warp), row_map(data, warp)

def sol01(data):

    x_map, y_map = extend(data, 2)

    galaxies = []
    for y, row in enumerate(data):
        for x, v in enumerate(row):
            if v == "#":
                galaxies.append((x_map[x], y_map[y]))

    pairs = combinations(galaxies, 2)
    res = []
    for a, b in pairs:
        res.append(abs(a[0] - b[0]) + abs(a[1] - b[1]))

    return sum(res)

def sol02(data):

    x_map, y_map = extend(data, 1000000)

    galaxies = []
    for y, row in enumerate(data):
        for x, v in enumerate(row):
            if v == "#":
                galaxies.append((x_map[x], y_map[y]))

    pairs = combinations(galaxies, 2)
    res = []
    for a, b in pairs:
        res.append(abs(a[0] - b[0]) + abs(a[1] - b[1]))

    return sum(res)


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)
    #print_data(DATA)

    SOL01 = sol01(DATA)
    print("SOL01: {}".format(SOL01))

    SOL02 = sol02(DATA)
    print("SOL02: {}".format(SOL02))

