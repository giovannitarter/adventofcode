#!/usr/bin/python
"""
solution file
"""

import sys
import copy
import time


def timeit(f):

    def timed(*args, **kw):

        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print(f"{f.__name__} took: {te-ts:.4f} sec")
        return result

    return timed


def parse_input(text):
    "input parsing function"
    res = [list(x) for x in text.split("\n") if x != ""]
    return res


def print_input(data):
    "data print function"
    # print(f"DATA:\n{data}\n")
    for d in data:
        print("".join(d))


def parse_pos(data):
    pos = {}
    for y, row in enumerate(data):
        for x, v in enumerate(row):
            if v not in ".#":
                tmp = pos.get(v, [])
                tmp.append((x, y))
                pos[v] = tmp
    return pos


def antinodes(a, b, data, first=True):

    if a[1] > b[1]:
        tmp = a
        a = b
        b = tmp

    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])

    i = 0
    res = []

    if first:
        Dx = dx
        Dy = dy
    else:
        Dx = 0
        Dy = 0

    #coeff = (a[0] - b[0]) // (a[0] - b[0])

    if a[0] < b[0]:

        while True:
            tmp = [(a[0] - Dx, a[1] - Dy), (b[0] + Dx, b[1] + Dy)]
            tmp = filter(
                    lambda a: -1 < a[0] < len(data[0])
                    and -1 < a[1] < len(data),
                    tmp
                    )
            tmp = list(tmp)
            res.extend(tmp)
            if len(tmp) == 0:
                return res

            if first:
                break

            Dx += dx
            Dy += dy
            i += 1
        return res

    else:
        while True:
            tmp = [(a[0] + Dx, a[1] - Dy), (b[0] - Dx, b[1] + Dy)]
            tmp = filter(
                    lambda a: -1 < a[0] < len(data[0])
                    and -1 < a[1] < len(data),
                    tmp
                    )
            tmp = list(tmp)
            res.extend(tmp)
            if len(tmp) == 0:
                return res

            if first:
                break

            Dx += dx
            Dy += dy
            i += 1
        return res


def all_antinodes(antennas, data, first=True):

    res = []
    for i, a in enumerate(antennas):
        for j, b in enumerate(antennas):
            if i < j:
                res.extend(antinodes(a, b, data, first))

    return res


@timeit
def sol01(data):
    "solution for part 1"

    ants = []
    pos = parse_pos(data)
    for p in pos:
        ants.extend(all_antinodes(pos[p], data))

    return len(set(ants))


@timeit
def sol02(data):
    "solution for part 2"

    #print(antinodes((4, 3), (5, 5), data))

    ants = []
    pos = parse_pos(data)
    for p in pos:
        all_ant = all_antinodes(pos[p], data, first=False)
        ants.extend(all_ant)

    ants = set(ants)
    # for x, y in ants:
    #     if data[y][x] == ".":
    #         data[y][x] = "#"
    # print_input(data)

    return len(ants)


if __name__ == "__main__":

    RES = None

    with open(sys.argv[1], encoding="utf8") as fd:
        TEXT = fd.read()

    DATA = parse_input(TEXT)
    # print_input(DATA)
    SOL01 = sol01(DATA)
    print(f"SOL01: {SOL01}")
    SOL02 = sol02(DATA)
    print(f"SOL02: {SOL02}")
