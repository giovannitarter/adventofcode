#!/usr/bin/python


import sys
import copy



def parse_input(text):

    res = None
    lines = [x for x in text.split("\n") if x != ""]

    return res


def sol01(data):
    res = None
    return res


def sol02(data):
    res = None
    return res


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)
    print(f"DATA:\n{DATA}\n")

    SOL01 = sol01(DATA)
    print("SOL01: {}".format(SOL01))
    
    SOL02 = sol02(DATA)
    print("SOL02: {}".format(SOL02))

