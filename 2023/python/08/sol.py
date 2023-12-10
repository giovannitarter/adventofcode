#!/usr/bin/python


import sys
import copy
import re
import math

def parse_input(text):

    res = None
    lines = [x for x in text.split("\n") if x != ""]

    dirs = list(lines[0].strip())

    nodes = {}
    for l in lines[1:]:
        m = re.match("([0-9A-Z]*) = \(([0-9A-Z]*), ([0-9A-Z]*)\)", l)
        if m:
            nodes[m.group(1)] = (m.group(2), m.group(3))

    return dirs, nodes


def sol01(data):

    dirs, nodes = data

    step = 0
    cpos = "AAA"
    while cpos != "ZZZ":
        cdir = dirs[step % len(dirs)]
        if cdir == "L":
            cpos = nodes[cpos][0]
        elif cdir == "R":
            cpos = nodes[cpos][1]

        step = step + 1

    return step


def find_loop(dirs, nodes, s):

    step = 0
    cpos = s
    while True:

        if cpos.endswith("Z"):
            return step

        cdir = dirs[step % len(dirs)]
        if cdir == "L":
            cpos = nodes[cpos][0]
        elif cdir == "R":
            cpos = nodes[cpos][1]

        step = step + 1
    return


def sol02(data):

    dirs, nodes = data
    srcs = [x for x in nodes if x.endswith("A")]
    return math.lcm(*[find_loop(dirs, nodes, s) for s in srcs])


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)
    #print(f"DATA:\n{DATA}\n")

    SOL01 = sol01(DATA)
    print("SOL01: {}".format(SOL01))

    SOL02 = sol02(DATA)
    print("SOL02: {}".format(SOL02))
