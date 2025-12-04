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
    res = [x for x in res[0].split(",") if x != ""]
    res = [re.match(r"([0-9]+)-([0-9]+)", x).groups() for x in res]
    res = [(int(x), int(y)) for x, y in res]
    return res


def print_input(data):
    "data print function"
    print(f"DATA:\n{data}\n")


def check_valid(v):

    v = str(v)

    low = v[:len(v) // 2]
    high = v[len(v) // 2:]

    return not (low == high)


#def generate_invalid_range()


@timeit
def sol01(data):
    "solution for part 1"
    res = []

    for s, e in data:
        # print("")
        for i in range(s, e+1):
            tmp = check_valid(i)
            if not tmp:
                # print(i)
                res.append(i)

    return sum(res)


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
    # print_input(DATA)
    SOL01 = sol01(copy.deepcopy(DATA))
    print(f"SOL01: {SOL01}")
    SOL02 = sol02(copy.deepcopy(DATA))
    print(f"SOL02: {SOL02}")
