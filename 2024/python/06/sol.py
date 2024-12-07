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
    return [list(x) for x in text.split("\n") if x != ""]


def print_input(data):
    "data print function"
    print(f"DATA:")
    for d in data:
        print("".join(d))


def get_initial(data):
    for x in range(len(data[0])):
        for y in range(len(data)):
            if data[y][x] not in ".#":
                return x, y, data[y][x]

    return


def next90(curr):
    seq90_clk = ["^", ">", "v", "<"]
    return seq90_clk[(seq90_clk.index(curr) + 1) % 4]


def opposite(c):
    return next90(next90(c))


def prog(direction):
    tbl = {
            "^": (0, -1),
            ">": (1, 0),
            "v": (0, 1),
            "<": (-1, 0)
        }
    return tbl[direction]


def step(pos, data):

    x, y, heading = pos
    dx, dy = prog(heading)

    nx, ny = x + dx, y + dy
    if -1 < nx < len(data[0]) and -1 < ny < len(data):
        if data[ny][nx] != "#":
            return nx, ny, heading
        else:
            return x, y, next90(heading)
    else:
        return None


@timeit
def sol01(data):
    "solution for part 1"

    tiles = set()
    pos = get_initial(data)
    tiles.add((pos[0], pos[1]))

    while True:

        pos = step(pos, data)
        if pos is None:
            break

        tiles.add((pos[0], pos[1]))

    return len(tiles)


def get_right_tiles(pos, data):

    res = []
    dx, dy = prog(next90(pos[2]))

    nx, ny = pos[0], pos[1]
    while -1 < nx < len(data[0]) and -1 < ny < len(data):

        res.append((nx, ny))
        if data[ny][nx] == "#":
            break
        nx, ny = nx + dx, ny + dy

    return res


#@timeit
#def sol02(data):
#    "solution for part 2"
#
#    tiles = {}
#    orig = get_initial(data)
#    obstructions = set()
#    #obstructions = []
#
#    data[orig[1]][orig[0]] = "."
#
#    pos = orig
#    tiles[(pos[0], pos[1])] = [pos[2]]
#    while True:
#
#        right_tiles = get_right_tiles(pos, data)
#
#        if len(right_tiles) > 1:
#            sx, sy = right_tiles[-1]
#            ox, oy = right_tiles[-2]
#
#            if data[sy][sx] == "#":
#                opp = opposite(pos[2])
#                if opp in tiles.get((ox, oy), []):
#                    tmp = step(pos, data)
#                    obstructions.add(tmp[:2])
#                    #print(pos)
#
#        pos = step(pos, data)
#        if pos is None:
#            break
#
#        key = (pos[0], pos[1])
#        t = tiles.get(key, [])
#        t.append(pos[2])
#        tiles[key] = t
#
#
#    for x, y in obstructions:
#        data[y][x] = "O"
#    print_input(data)
#
#    # 730 too low
#    # 731 too low
#    # 732 too low
#
#    return len(obstructions)


def check_loop(data, pos):
    tiles = set()
    tiles.add(pos)

    while True:

        pos = step(pos, data)
        if pos is None:
            break

        if pos in tiles:
            return True

        tiles.add(pos)

    return False


@timeit
def sol02(data):

    tiles = set()
    pos = get_initial(data)
    tiles.add((pos[0], pos[1]))

    while True:

        pos = step(pos, data)
        if pos is None:
            break

        tiles.add((pos[0], pos[1]))

    init = get_initial(data)

    res = 0
    for x, y in tiles:
        ndata = [list(d) for d in data]
        ndata[y][x] = "#"

        if check_loop(ndata, init):
            res += 1

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
