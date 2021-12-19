#!/usr/bin/python


import sys
import re
from collections import namedtuple


Region = namedtuple("Region", ["xl", "xh", "yl", "yh"])


def parse_input(text):

    res = None
    lines = [ x for x in text.split("\n") if x != "" ]
    
    m = re.match(r"target area: x=([-\d]+)..([-\d]+), y=([-\d]+)..([-\d]+)", lines[0])
    
    res = [ int(x) for x in m.groups() ]
    res = Region(*res)
    
    return res


def simulate(sx, sy, region):

    x = 0
    y = 0
    max_y = y
    hit = False

    s = 0
    while y >= region.yl and x <= region.xh:
        
        #print(f"step {s}: x:{x}, y:{y}")
        
        x = x + sx
        y = y + sy

        if y > max_y:
            max_y = y

        if x >= region.xl and x <= region.xh and y >= region.yl and y <= region.yh:
            hit = True

        if sx > 0:
            sx -= 1
        elif sx < 0:
            sx += 1

        sy -= 1

        s = s + 1

    res = hit, max_y
    return res


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)
    print(DATA)
            
    INI_VEL = set()

    max_y = 0
    for sx in range(0, DATA.xh + 1):
        for sy in range(DATA.yl, -DATA.yl + 1):
            tmp = simulate(sx, sy, DATA)
            if tmp[0]:
                
                INI_VEL.add((sx, sy))
                if tmp[1] > max_y:
                    max_y = tmp[1]

    RES = max_y
    print("sol01 : {}".format(RES))

    RES = len(INI_VEL)
    print("sol02 : {}".format(RES))

