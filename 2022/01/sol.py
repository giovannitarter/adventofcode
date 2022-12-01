#!/usr/bin/python


import sys
import copy



def parse_input(text):
    res = [sum([int(f) for f in x.split("\n") if f != ""]) for x in text.split("\n\n")]
    res.sort()
    return res


def sol01(data):
    res = data[-1]
    return res


def sol02(data):
    res = sum(data[-3:])
    return res


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)
    
    RES = sol01(DATA)
    print("sol01 : {}".format(RES))
    
    RES = sol02(DATA)
    print("sol02 : {}".format(RES))
