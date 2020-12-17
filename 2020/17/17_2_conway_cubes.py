#!/usr/bin/python

import sys
import itertools


elem = [-1, 0, 1]
neigh = []
for i in elem:
    for j in elem:
        for k in elem:
            for m in elem:
                neigh.append((i,j,k,m))
neigh.remove((0, 0, 0, 0))
neigh_mat = neigh.copy()


def get_all_neigh(pos, neigh_mat):

    res = []
    for x, y, z, m in neigh_mat:
        n = ((pos[0] + x, pos[1] + y, pos[2] + z, pos[3] + m))
        res.append(n)

    return res


def get_active(pos, space):

    res = 0
    neigh = get_all_neigh(pos, neigh_mat)
    #print(neigh)

    for n in neigh:
        curr = space.get(n, ".")
        if curr == "#":
            res += 1

    return res


def cycle(space):

    new_space = space.copy()

    eval_points = set(space.keys())
    for pos in space:
        neigh = get_all_neigh(pos, neigh_mat)
        for n in neigh:
            eval_points.add(n)

    for pos in eval_points:

        #print("\npos: {}".format(pos))

        curr = space.get(pos, ".")
        active = get_active(pos, space)
        #print(active)

        if curr == "#":
            if not(active == 2 or active == 3):
                new_space[pos] = "."

        elif curr == ".":
            if active == 3:
                new_space[pos] = "#"

    return new_space


def ax_bound(ax_nr, space):
    points = [p[ax_nr] for p in space.keys()]
    min_p = min(points)
    max_p = max(points) + 1
    return (min_p, max_p)


def count_active(space):
    res = 0
    for p in space:
        if space[p] == "#":
            res += 1

    return res



##################################
# MAIN
##################################


fd = open(sys.argv[1])
text = fd.read()
fd.close()

lines = text.split("\n")
lines = [l for l in lines if l != ""]

space = {}
for y, l in enumerate(lines):
    for x, v in enumerate(l):
        pos = (x, y, 0, 0)
        space[pos] = v

for r in range(1, 7):
    space = cycle(space)
    print("cycle {}, count: {}".format(r, count_active(space)))

