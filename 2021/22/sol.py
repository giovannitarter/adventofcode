#!/usr/bin/python


import sys
import copy
import re
from collections import namedtuple
import itertools


Cuboid = namedtuple("Cuboid", ["x1", "x2", "y1", "y2", "z1", "z2"])

def parse_input(text):

    res = []
    lines = [ x for x in text.split("\n") if x != "" ]
    for l in lines:
        m = re.match("(\w+) x=([-\d]+)..([-\d]+),y=([-\d]+)..([-\d]+),z=([-\d]+)..([-\d]+)", l)
        
        c = Cuboid(*[int(x) for x in m.groups()[1:]])
        if m[1] == "on":
            cmd = [True, c]
        else:
            cmd = [False, c]

        res.append(cmd)
    
    return res


def execute_cmd(space, cmd):

    act, cbd = cmd
    
    new_cbd = Cuboid(
            max(cbd.x1, -50),
            min(cbd.x2, 51),
            max(cbd.y1, -50),
            min(cbd.y2, 51),
            max(cbd.z1, -50),
            min(cbd.z2, 51)
            )
    
    if new_cbd.x2>=new_cbd.x1 and new_cbd.y2>=new_cbd.y1 and new_cbd.z2>=new_cbd.z1:
        new_cmd = [act, new_cbd]
        res = execute_cmd2(space, new_cmd)
    else:
        res = space
    
    return res


def intersect(a, b): 
    res = not (
            b.x1 > a.x2 or
            b.x2 < a.x1 or
            b.y1 > a.y2 or
            b.y2 < a.y1 or
            b.z1 > a.z2 or
            b.z2 < a.z1 
            )
    return res


def split_cuboid(ap, b):

    res = []
        
    a = Cuboid(ap.x1, ap.x2, ap.y1, ap.y2, ap.z1, ap.z2)
    
    if a.x1 <= b.x2 <= a.x2:
        res.append(Cuboid(b.x2+1, a.x2,   a.y1,   a.y2,   a.z1,   a.z2  ))
        a = Cuboid(a.x1, b.x2, a.y1, a.y2, a.z1, a.z2)
    
    if a.x1 <= b.x1 <= a.x2:
        res.append(Cuboid(a.x1,   b.x1-1, a.y1,   a.y2,   a.z1,   a.z2  ))
        a = Cuboid(b.x1, a.x2, a.y1, a.y2, a.z1, a.z2)
    
    if a.y1 <= b.y2 <= a.y2:
        res.append(Cuboid(a.x1,   a.x2,   b.y2+1, a.y2,   a.z1,   a.z2  ))
        a = Cuboid(a.x1, a.x2, a.y1, b.y2, a.z1, a.z2)
    
    if a.y1 <= b.y1 <= a.y2:
        res.append(Cuboid(a.x1,   a.x2,   a.y1,   b.y1-1, a.z1,   a.z2  ))
        a = Cuboid(a.x1, a.x2, b.y1, a.y2, a.z1, a.z2)
    
    if a.z1 <= b.z2 <= a.z2:
        res.append(Cuboid(a.x1,   a.x2,   a.y1,   a.y2,   b.z2+1, a.z2  ))
        a = Cuboid(a.x1, a.x2, a.y1, a.y2, a.z1, b.z2)
    
    if a.z1 <= b.z1 <= a.z2:
        res.append(Cuboid(a.x1,   a.x2,   a.y1,   a.y2,   a.z1,   b.z1-1))
        a = Cuboid(a.x1, a.x2, a.y1, a.y2, b.z1, a.z2)

    res = [c for c in res if c.x2>=c.x1 and c.y2>=c.y1 and c.z2>=c.z1]

    return res


def count(space):

    res = 0
    for c in space:
        vol = (c.x2 - c.x1 + 1) * (c.y2 - c.y1 + 1) * (c.z2 - c.z1 + 1)
        res += vol

    return res


def execute_cmd2(space, cmd):
    
    res = []
    
    act, cub_b = cmd
    
    if len(space) == 0:
        if act:
            return [cub_b]
        else:
            return []

    for cub_a in space:    
        if not intersect(cub_a, cub_b):
            res.append(cub_a)
        else:
            split_res = split_cuboid(cub_a, cub_b)
            res.extend(split_res)
        
    if act:
        res.append(cub_b)

    return res


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()


    DATA = parse_input(TEXT)

    SPACE = []
    for d in DATA:
        SPACE = execute_cmd(SPACE, d)
    CNT= count(SPACE)
    print(f"sol01: {CNT}")
    
    SPACE = []
    for d in DATA:
        SPACE = execute_cmd2(SPACE, d)
    CNT= count(SPACE)
    print(f"sol02: {CNT}")

