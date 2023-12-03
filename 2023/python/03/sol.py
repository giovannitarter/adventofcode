#!/usr/bin/python


import sys
import copy
import re
from functools import reduce


mask = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
]

def parse_input(text):

    res = None
    lines = [x for x in text.split("\n") if x != ""]

    numbers = []
    symbols = []
    for y, l in enumerate(lines):
        for m in re.finditer("(\d+)", l):
            pos = [(x,y) for x in range(*m.span())]
            nr = int(m.group(0))
            numbers.append((nr, pos))
        
        for m in re.finditer("([^\d\.])", l):
            symbols.append((m.group(0), (m.start(), y)))

    return numbers, symbols


def part_neigh(pos):
    neigh = []
    for dx, dy in pos:
        neigh.extend([(dx+x, dy+y) for x,y in mask])
    
    neigh = [(x, y) for x, y in neigh if x > -1 and y > -1 and (x,y) not in pos]
    neigh = set(neigh)
    return neigh


def sol01(data):
    
    res = 0
    numbers, symbols = data

    spos = set([p for s, p in symbols])
    for n, pos in numbers:
        neigh = part_neigh(pos)
        if spos.intersection(neigh):
            res += n

    return res


def product(l):
    return reduce((lambda x, y: x * y), l)

def sol02(data):
    res = 0
    numbers, symbols = data

    gear_neigh = {}
    for g in [p for s, p in symbols if s == "*" ]:
        for n, pos in numbers:
            neigh = part_neigh(pos)
            if g in neigh:
                tmp = gear_neigh.get(g, [])
                tmp.append(n)
                gear_neigh[g] = tmp

    ratios = [product(gear_neigh[l]) for l in gear_neigh if len(gear_neigh[l]) == 2]
    res = sum(ratios)
    return res


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)
    #print(f"DATA:\n{DATA}\n")
    
    #for n, pos in numbers:
    #    print(f"n: {n} -> {pos}")
    
    #for s, pos in symbols:
    #    print(f"s: {s} -> {pos}")

    SOL01 = sol01(DATA)
    print("SOL01: {}".format(SOL01))
    
    SOL02 = sol02(DATA)
    print("SOL02: {}".format(SOL02))

