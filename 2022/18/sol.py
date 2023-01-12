#!/usr/bin/python


import sys
import copy
import itertools


mask = [
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1),
        (-1, 0, 0),
        (0, -1, 0),
        (0, 0, -1),
        ]


def neighbors(c):
    res = [(c[0]+xm, c[1]+ym, c[2]+zm) for (xm, ym, zm) in mask]
    return res


def parse_input(text):
    return set([tuple(map(int, x.split(","))) for x in text.split("\n") if x != ""])


def sol01(data):

    res = 6 * len(data)

    for d in data:
        neigh = neighbors(d)
        for n in neigh:
            if n in data:
                res -= 1

    return res


def neighbors2(c, data, minc, maxc):

    res = []
    for n in neighbors(c):

        if any(map(lambda x: x < minc or x >= maxc, n)):
            continue

        if n in data:
            continue

        res.append(n)

    return res



def dfs(data, s, minc, maxc):

    visited = set()
    q = [s]

    while q:
        v = q.pop()
        if v not in visited:
            visited.add(v)
            for w in neighbors2(v, data, minc, maxc):
                q.append(w)

    return visited


def sol02(data):

    #adding an empty externah hull
    maxc = max([max([d[i] for d in data]) for i in range(3)]) + 2
    minc = min([min([d[i] for d in data]) for i in range(3)]) - 1

    span = range(minc, maxc)
    external = dfs(data, (minc, minc, minc), minc, maxc)

    all_c = set(itertools.product(span, span, span))
    internal = all_c.difference(external).difference(data)

    ext_faces = sol01(data)
    internal_faces = sol01(internal)

    res = ext_faces - internal_faces
    return res


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)
    #print(f"DATA:\n{DATA}\n")
    #for d in DATA:
    #    print(d)

    SOL01 = sol01(DATA)
    print("SOL01: {}".format(SOL01))

    SOL02 = sol02(DATA)
    print("SOL02: {}".format(SOL02))

