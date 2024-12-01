#!/usr/bin/python


import sys
import copy
import math



def parse_input(text):

    lines = [x.split() for x in text.split("\n") if x != ""]
    lines = zip(*lines)
    lines = [list(map(int, l)) for l in lines]
    return lines


def print_input(data):
    print(f"DATA:\n{data}\n")
    return


def sol01(data):

    a = sorted(list(data[0]))
    b = sorted(list(data[1]))

    diff = [abs(b- a) for a, b in zip(a, b)]
    return sum(diff)


def sol02(data):
    counts = {a:data[1].count(a) for a in data[0]}
    return sum(k*counts[k] for k in data[0])


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)
    #print_input(DATA)

    SOL01 = sol01(DATA)
    print("SOL01: {}".format(SOL01))

    SOL02 = sol02(DATA)
    print("SOL02: {}".format(SOL02))

