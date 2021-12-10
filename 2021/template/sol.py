#!/usr/bin/python


import sys
import copy



def parse_input(text):

    res = None
    lines = [ x for x in text.split("\n") if x != "" ]

    return res


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)

    print("res : {}".format(RES))
