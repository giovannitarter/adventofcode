#!/usr/bin/python


import sys
import copy
import re



def parse_input(text):

    res = None
    res = [re.match(r"(\d+)-(\d+),(\d+)-(\d+)", x) for x in text.split("\n") if x != ""]
    res = [(int(x[1]), int(x[2]), int(x[3]), int(x[4])) for x in res]
    return res


def contain(l1, h1, l2, h2):
    return l1 <= l2 and h1 >=h2


def overlaps(l1, h1, l2, h2):
    return l2 <= h1 and l1 <= h2


def sol01(data):
    res = 0
    for l1, h1, l2, h2 in data:
        if contain(l1, h1, l2, h2) or contain(l2, h2, l1, h1):
            res += 1
            #print(f"{l1}-{h1},{l2}-{h2}")
    return res


def sol02(data):
    res = 0
    for l1, h1, l2, h2 in data:
        if overlaps(l1, h1, l2, h2):
            #print(f"{l1}-{h1},{l2}-{h2}")
            res += 1
    return res


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)
    
    SOL01 = sol01(DATA)
    print("sol01 : {}".format(SOL01))
    
    SOL02 = sol02(DATA)
    print("sol02 : {}".format(SOL02))

