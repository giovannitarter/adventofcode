#!/usr/bin/python
"""
solution file
"""

import sys
import copy
import time


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
    return res


def print_input(data):
    "data print function"
    print(f"DATA:\n{data}\n")


@timeit
def sol01(data):
    "solution for part 1"
    res = None
    return res


@timeit
def sol02(data):
    "solution for part 2"
    res = None
    return res


if __name__ == "__main__":

    RES = None

    with open(sys.argv[1], encoding="utf8") as fd:
        TEXT = fd.read()

    DATA = parse_input(TEXT)
    print_input(DATA)
    SOL01 = sol01(copy.deepcopy(DATA))
    print(f"SOL01: {SOL01}")
    SOL02 = sol02(copy.deepcopy(DATA))
    print(f"SOL02: {SOL02}")
