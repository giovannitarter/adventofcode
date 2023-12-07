#!/usr/bin/python


import math
import sys
import copy
from functools import reduce


def parse_input(text):
    return [x for x in text.split("\n") if x != ""]


def parse1(lines):

    def parse_line(l):
        res = (l.split(":"))[1].strip()
        return [int(x) for x in res.split()]

    return (parse_line(lines[0]), parse_line(lines[1]))

def parse2(lines):

    time = int((lines[0].split(":"))[1].replace(" ", ""))

    dist = int((lines[1].split(":"))[1].replace(" ", ""))
    return time, dist

#def calc_ways(race_len, ref_dist):
#
#    w = []
#    for t in range(race_len):
#        bdist = t * (race_len-t)
#        if bdist > ref_dist:
#            w.append(t)
#
#    return(len(w))


def calc_ways(T, D):

    D = D + 0.001
    x1 = math.ceil(((-T + math.sqrt(math.pow(T, 2) - 4*D)) / -2))
    x2 = math.floor(((-T - math.sqrt(math.pow(T, 2) - 4*D)) / -2))
    res = x2 - x1 + 1
    return res



def sol01(data):

    res = []
    time, dist = parse1(data)
    for idx, race_len in enumerate(time):
        ref_dist = dist[idx]
        res.append(calc_ways(race_len, ref_dist))

    res = reduce((lambda x, y: x * y), res)
    return res


def sol02(data):
    res = calc_ways(*parse2(data))
    return res


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

