#!/usr/bin/python


import sys


def count_trees(lines, right, down):

    max_x = len(lines[0])
    x = 0
    y = 0
    trees = 0
    while y < len(lines):
        if lines[y][x] == "#":
            trees = trees + 1
        y = y + down
        x = (x + right) % max_x
    return trees


fd = open(sys.argv[1], "r")
text = fd.read()
fd.close()

lines = text.split("\n")
lines = list(filter(lambda x: x != "", lines))

#for l in lines:
#    print(l)



pars = [(1,1), (3,1), (5,1), (7,1), (1,2)]
res = []
for p in pars:
    right, down = p
    tmp = count_trees(lines, right, down)
    print("par: {} -> {}".format(p, tmp))
    res.append(tmp)


mul = 1
for r in res:
    mul = mul * r

print(mul)

