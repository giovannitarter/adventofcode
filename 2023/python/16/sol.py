#!/usr/bin/python
"""
solution file
"""

import sys
import copy


def parse_input(text):
    "input parsing function"
    res = [list(x) for x in text.split("\n") if x != ""]
    return res


def print_input(data):
    "data print function"

    for d in data:
        print("".join(d))


def follow_beam(beam, data):

    beams = []
    x, y, dx, dy = beam

    tiles = copy.deepcopy(data)
    tiles[y][x] = "#"

    tiles_idx = set()
    visited = set()

    while True:


        if (x, y, dx, dy) in visited:
            break

        if 0 <= x < len(data[0]) and 0 <= y < len(data):

            visited.add((x, y, dx, dy))
            tiles_idx.add((x, y))
            t = data[y][x]

            if t == "|" and dx in [1, -1]:
                beams.extend([(x, y, 0, -1), (x, y, 0, 1)])
                break
            elif t == "-" and dy in [1, -1]:
                beams.extend([(x, y, 1, 0), (x, y, -1, 0)])
                break
            elif t == "\\" and dx == 1:
                dx = 0
                dy = 1
            elif t == "\\" and dx == -1:
                dx = 0
                dy = -1
            elif t == "\\" and dy == 1:
                dx = 1
                dy = 0
            elif t == "\\" and dy == -1:
                dx = -1
                dy = 0
            elif t == "/" and dx == 1:
                dy = -1
                dx = 0
            elif t == "/" and dx == -1:
                dy = 1
                dx = 0
            elif t == "/" and dy == 1:
                dy = 0
                dx = -1
            elif t == "/" and dy == -1:
                dx = 1
                dy = 0

            x, y = x + dx, y + dy
        else:
            break

    return beams, tiles_idx


def print_data_tiles(data, tiles):

    tmp = copy.deepcopy(data)
    for x, y in tiles:
        tmp[y][x] = "X"

    print_input(tmp)




def sol01(data):
    "solution for part 1"

    beams = []
    beams.append((0, 0, 1, 0))
    cache = {}
    tiles = set()

    while beams:

        c_beam = beams.pop(0)

        new_beams, new_tiles = follow_beam(c_beam, data)
        cache[c_beam] = True

        new_beams = [b for b in new_beams if b not in cache]
        beams.extend(new_beams)

        tiles = tiles.union(new_tiles)

    return len(tiles)


def sol02(data):
    "solution for part 2"
    res = None
    return res


if __name__ == "__main__":

    RES = None

    with open(sys.argv[1], encoding="utf8") as fd:
        TEXT = fd.read()

    DATA = parse_input(TEXT)
    #print_input(DATA)

    SOL01 = sol01(DATA)
    print(f"SOL01: {SOL01}")

    SOL02 = sol02(DATA)
    print(f"SOL02: {SOL02}")
