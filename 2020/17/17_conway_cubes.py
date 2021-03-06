#!/usr/bin/python

import sys
import itertools


elem = [-1, 0, 1]
neigh = []
for i in elem:
    for j in elem:
        for k in elem:
            neigh.append((i,j,k))
neigh.remove((0, 0, 0))
neigh_mat = neigh.copy()


def get_all_neigh(pos, neigh_mat):

    res = []
    for x, y, z in neigh_mat:
        n = ((pos[0] + x, pos[1] + y, pos[2] + z))
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

    #print("all_points:", len(eval_points))

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

        #print("neigh({}) : {}".format(pos, neigh))

    return new_space


def ax_bound(ax_nr, space):
    points = [p[ax_nr] for p in space.keys()]
    min_p = min(points)
    max_p = max(points) + 1
    return (min_p, max_p)


def print_space(space):
    #print(space)
    #print(ax_bound(1, space))

    for z in range(*ax_bound(2, space), 1):
        print("\nz={}".format(z))
        for y in range(*ax_bound(1, space), 1):
            row = []
            for x in range(*ax_bound(0, space), 1):
                row.append(space.get((x,y,z), "."))
            print("".join(row))

    return


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

#for l in lines:
#    print(l)



space = {}
for y, l in enumerate(lines):
    for x, v in enumerate(l):
        pos = (x, y, 0)
        space[pos] = v

#for n in neigh:
#    print(n)




print_space(space)

#print(get_all_neigh((1, 2, 3), neigh_mat))

#print(get_active((1, 1, 0), space))

for r in range(1, 7):
    space = cycle(space)
    print("cycle {}, count: {}".format(r, count_active(space)))

#print_space(space)

#print(space)
