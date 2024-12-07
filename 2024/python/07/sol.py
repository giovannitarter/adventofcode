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
    res = [tuple(x.split(":")) for x in text.split("\n") if x != ""]
    return [(int(a), tuple(map(int, b.strip().split()))) for a, b in res]


def print_input(data):
    "data print function"
    print(f"DATA:\n{data}\n")


def try_operators(res, vals):

    if len(vals) == 1:
        return vals[0] == res

    else:
        return any(
                [
                    try_operators(res, (vals[0] + vals[1], *vals[2:])),
                    try_operators(res, (vals[0] * vals[1], *vals[2:]))
                ]
                )


def try_operators2(res, vals):

    if len(vals) == 1:
        return vals[0] == res

    elif vals[0] > res:
        return False

    else:
        return any(
                [
                    try_operators2(res, (vals[0] + vals[1], *vals[2:])),
                    try_operators2(res, (vals[0] * vals[1], *vals[2:])),
                    try_operators2(res,
                                  (int(str(vals[0]) + str(vals[1])), *vals[2:])
                                  )
                ]
                )


@timeit
def sol01(data):
    "solution for part 1"
    return sum(list(map(lambda d: d[0] if try_operators(*d) else 0, data)))


@timeit
def sol02(data):
    "solution for part 2"
    return sum(list(map(lambda d: d[0] if try_operators2(*d) else 0, data)))


if __name__ == "__main__":

    RES = None

    with open(sys.argv[1], encoding="utf8") as fd:
        TEXT = fd.read()

    DATA = parse_input(TEXT)
    # print_input(DATA)
    SOL01 = sol01(DATA)
    print(f"SOL01: {SOL01}")
    SOL02 = sol02(DATA)
    print(f"SOL02: {SOL02}")
