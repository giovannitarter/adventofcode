#!/usr/bin/python

import sys
import re

transforms = {
        "e" : (1, -1, 0),
        "se" : (0, -1, 1),
        "sw" : (-1, 0, 1),
        "w" : (-1, 1, 0),
        "nw" : (0, 1, -1),
        "ne" : (1, 0, -1),
    }


def parse_line(line):

    res = []
    rxp = "|".join(transforms.keys())

    #print("")
    #print(line)

    res = re.findall(rxp, line)
    #print(res)

    return res


def neighbors(t):
    res = []
    for r0, r1, r2 in transforms.values():
        res.append((t[0] + r0, t[1] + r1, t[2] + r2))
    return res


def round(tiles):

    new = dict(tiles)

    for ctile in tiles:
        neigh = neighbors(ctile)
        for n in neigh:
            nval = tiles.get(n, "w")
            new[n] = nval

    tiles = new
    new = dict(tiles)

    for ctile in tiles:
        cval = tiles.get(ctile, "w")
        neigh = neighbors(ctile)
        neigh_val = [tiles.get(x, "w") for x in neigh]

        nval = cval
        if cval == "b":
            if neigh_val.count("b") == 0 or neigh_val.count("b") > 2:
                nval = "w"
        elif cval == "w":
            if neigh_val.count("b") == 2:
                nval = "b"

        new[ctile] = nval

    return new



def count_black(tiles):
    acc = 0
    for t in tiles:
        if tiles[t] == "b":
            acc += 1
    return acc


fd = open(sys.argv[1])
text = fd.read()
fd.close()


lines = text.split("\n")
lines = [l for l in lines if l != ""]


directions = []


for l in lines:
    directions.append(parse_line(l))


tiles = {}

for d_seq in directions:

    cpos = (0, 0, 0)
    for d in d_seq:
        t0, t1, t2 = transforms[d]
        cpos = (cpos[0] + t0, cpos[1] + t1, cpos[2] + t2)

    #print("cpos: {}".format(cpos))
    dest = tiles.get(cpos, "w")
    if dest == "w":
        dest = "b"
    else:
        dest = "w"

    tiles[cpos] = dest

#print(len(tiles.keys()))

sol1 = count_black(tiles)

print("SOL1: {}".format(sol1))


for i in range(1, 101):

    tiles = round(tiles)
    black = count_black(tiles)
    print("Day {}: {}".format(i, black))




#print(tiles)


