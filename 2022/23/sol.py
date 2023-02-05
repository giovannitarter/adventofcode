#!/usr/bin/python


import sys
import copy

D = {
    "N"  : ( 0, -1),
    "NE" : ( 1, -1),
    "E"  : ( 1,  0),
    "SE" : ( 1,  1),
    "S"  : ( 0,  1),
    "SW" : (-1,  1),
    "W"  : (-1,  0),
    "NW" : (-1, -1),
}

for k in D:
    exec(f"{k} = {D[k]}")

directions = {
        0: ([N, NE, NW], (0, -1)),
        1: ([S, SE, SW], (0,  1)),
        2: ([W, NW, SW], (-1, 0)),
        3: ([E, NE, SE], (1,  0)),
        }


def parse_input(text):

    mat = [list(x) for x in text.split("\n") if x != ""]

    res = set()
    for y, row in enumerate(mat):
        for x, v in enumerate(row):
            if v == "#":
                res.add((x, y))

    return res


def print_data(data):
    print(f"DATA:\n")
    for d in data:
        print(f"{d}")
    print("")
    return


def print_map(data):

    xs = [x for x, y in data]
    ys = [y for x, y in data]

    min_x = min(xs)
    min_y = min(ys)
    max_x = max(xs) + 1
    max_y = max(ys) + 1

    mat = []
    for y in range(min_y, max_y):
        row = ["." for _ in range(min_x, max_x)]
        mat.append(row)

    for x, y in data:
        mat[y-min_y][x-min_x] = "#"

    for row in mat:
        print("".join(row))

    return



def mov_round(data, round_nr):


    proposals = {}
    for x, y in sorted(data):

        #print(f"elf: {x} {y}")

        adj_elv = [(x + xd, y + yd) for (xd, yd) in D.values() if (x+xd, y+yd) in data]
        if not adj_elv:
            continue

        for d in range(4):
            cond, step = directions[(round_nr + d) % 4]
            elves_dir = [(x + cx, y + cy) for cx, cy in cond if (x+cx, y+cy) in data]

            #print(f"   {(round_nr + d) % 4} -> {elves_dir}")
            if elves_dir:
                continue

            sx = x + step[0]
            sy = y + step[1]
            p = proposals.get((sx, sy), [])
            p.append((x, y))
            proposals[(sx, sy)] = p
            break

    #print(f"proposals: {proposals}")

    #phase 2
    res = set(data)
    for p in proposals:
        if len(proposals[p]) == 1:
            res.remove(proposals[p][0])
            res.add(p)

    return res


def compute_res(data):

    xs = [x for x, y in data]
    ys = [y for x, y in data]

    min_x = min(xs)
    min_y = min(ys)
    max_x = max(xs) + 1
    max_y = max(ys) + 1

    #print(f"x: {min_x} {max_x}")
    #print(f"y: {min_y} {max_y}")

    res = (max_x - min_x) * (max_y - min_y) - len(data)
    return res


def sol01(data):

    for i in range(10):

        #print(f"\nRound {i}")
        #print_map(data)
        #print(len(data))
        data = mov_round(data, i)

    res = compute_res(data)
    return res


def sol02(data):

    res = 0

    while True:

        new_data = mov_round(data, res)
        if new_data == data:
            break

        data = new_data
        res += 1

    return res + 1


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)
    #print_data(DATA)

    # 4115 too high
    SOL01 = sol01(DATA)
    print("SOL01: {}".format(SOL01))

    SOL02 = sol02(DATA)
    print("SOL02: {}".format(SOL02))

