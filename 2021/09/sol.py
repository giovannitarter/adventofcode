#!/usr/bin/python


import sys
import copy


cmap = {
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
}

def parse_input(text):

    res = []
    lines = [ x for x in TEXT.split("\n") if x != "" ]

    for l in lines:
        row = list(l)
        row = [int(x) for x in row]
        res.append(row)

    return res


def adj_list(x, y, max_x, max_y):

    res = []

    for ax, ay in cmap:
        cx = x + ax
        cy = y + ay

        if cx > -1 and cy > -1 and cx < max_x and cy < max_y:
            res.append((cx, cy))
    return res


def lowpoints(hmap):

    res = []

    for y, row in enumerate(hmap):
        for x, val in enumerate(row):
            adj = adj_list(x, y, len(hmap[0]), len(hmap))
            adj_values = [hmap[y][x] for x, y in adj]

            if val < min(adj_values):
                res.append((x, y))

    return res


def sol01(hmap, lowpoints):

    res = 0
    for x, y in lowpoints:
        res += 1 + hmap[y][x]

    return res


def get_basin(hmap, lp):

    res = set()

    q = set([lp])
    while len(q) > 0:

        v = q.pop()
        res.add(v)
        neigh = adj_list(v[0], v[1], len(hmap[0]), len(hmap))

        for a in neigh:
            x, y = a

            if hmap[y][x] == 9:
                continue

            if a not in res:
                q.add(a)

    res = list(res)
    return res


def compute_basins(hmap, lowpoints):

    basins = []

    for lp in lowpoints:
        bas = get_basin(hmap, lp)
        basins.append(bas)

    return basins


def sol02(basins_list):
    basins_list.sort(key=lambda x: len(x), reverse=True)

    res = 1
    for x in [len(x) for x in basins_list[0:3]]:
        res = res * x

    return res



if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1], encoding="utf-8")
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)
    LP = lowpoints(DATA)

    RES = sol01(DATA, LP)

    print(f"res01 : {RES}")

    BAS = compute_basins(DATA, LP)
    RES = sol02(BAS)
    print(f"res02 : {RES}")
