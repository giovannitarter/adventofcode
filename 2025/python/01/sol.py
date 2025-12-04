#!/usr/bin/python
"""
solution file
"""

import sys
import copy
import time
import re


def timeit(f):

    def timed(*args, **kw):

        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print(f"{f.__name__} took: {te-ts:.4f} sec")
        return result

    return timed


def parse_input(text):
    "input parsing function"
    res = [x for x in text.split("\n") if x != ""]

    def parse(x):
        a, b = re.match(r"([LR])([\d]+)", x).groups()
        return a, int(b)

    res = list(map(lambda x: parse(x), res))
    return res


def print_input(data):
    "data print function"
    print(f"DATA:\n{data}\n")


@timeit
def sol01(data):
    "solution for part 1"

    res = 0
    acc = 50
    for d, v in data:

        if d == "R":
            acc = (acc + v) % 100
        elif d == "L":
            acc = (acc - v) % 100
        else:
            print("Undef")
            exit(0)

        if acc == 0:
            res += 1

    return res


@timeit
def sol02(data):
    "solution for part 2"

    res = 0
    acc = 50

    for d, v in data:

        # speed up bruteforce a bit
        res += (v // 100)
        v = v % 100

        for i in range(v):
            if d == "L":
                acc = (acc - 1) % 100
            else:
                acc = (acc + 1) % 100

            if acc == 0:
                res += 1

    return res


#@timeit
#def sol02(data):
#    "solution for part 2"
#
#    res = 0
#    acc = 50
#
#    for d, v in data:
#
#        if d == "L":
#            res += abs((acc - v) // 100)
#            acc = (acc - v) % 100
#        elif d == "R":
#            res += (acc + v) // 100
#            acc = (acc + v) % 100
#        else:
#            print("Undef")
#            exit(1)
#
#        if acc == 0:
#            res += 1
#
#    return res


if __name__ == "__main__":

    RES = None

    with open(sys.argv[1], encoding="utf8") as fd:
        TEXT = fd.read()

    DATA = parse_input(TEXT)
    # print_input(DATA)
    SOL01 = sol01(copy.deepcopy(DATA))
    print(f"SOL01: {SOL01}")
    SOL02 = sol02(copy.deepcopy(DATA))
    print(f"SOL02: {SOL02}")

