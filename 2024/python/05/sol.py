#!/usr/bin/python
"""
solution file
"""

import sys
import copy
import time
from functools import cmp_to_key


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

    rules, updates = text.split("\n\n")

    def parse(text, sep):
        return [tuple(map(int, r.split(sep))) for r in text.split("\n") if r]

    return parse(rules, "|"), parse(updates, ",")



def print_input(data):
    "data print function"
    rules, updates = data
    print("\n".join([str(r) for r in rules]))
    print("\n".join([str(u) for u in updates]))


@timeit
def sol01(data):
    "solution for part 1"

    rules, updates = data
    res = []

    for u in updates:
        res_update = True
        for a, b in rules:
            if a in u and b in u:
                if u.index(a) > u.index(b):
                    res_update = False
                    break
        if res_update:
            res.append(u[len(u) // 2])

    return sum(res)


@timeit
def sol02(data):
    "solution for part 2"

    rules, updates = data
    res = []

    def compare(a, b):
        if a == b:
            return 0
        elif (a, b) in rules:
            return -1
        else:
            return 1

    for u in updates:
        tmp = sorted(u, key=cmp_to_key(compare))
        if tuple(u) != tuple(tmp):
            res.append(tmp[len(tmp) // 2])

    return sum(res)


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
