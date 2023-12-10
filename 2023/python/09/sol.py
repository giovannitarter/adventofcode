#!/usr/bin/python


import sys
import copy
from functools import reduce



def parse_input(text):
    return [
        [int(v) for v in x.split()]
        for x in text.split("\n") if x != ""
        ]


def calc_next(values):

    stack = [list(values)]
    while not all([v == 0 for v in stack[-1]]):
        stack.append([y-x for x, y in zip(stack[-1][:-1], stack[-1][1:])])

    #val = stack[-1][-1]
    #for l in stack[::-1][1:]:
    #    val = val + l[-1]
    #return val

    lasts = [x[-1] for x in stack[::-1]]
    return reduce(lambda a, b: a + b, lasts)



def calc_prev(values):

    stack = [list(values)]
    while not all([v == 0 for v in stack[-1]]):
        stack.append([y-x for x, y in zip(stack[-1][:-1], stack[-1][1:])])

    firsts = [x[0] for x in stack[::-1]]
    return reduce(lambda a, b: b - a, firsts)


def sol01(data):
    return sum([calc_next(d) for d in data])


def sol02(data):
    return sum([calc_prev(d) for d in data])


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

