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
    res = map(lambda x: list(x), res)
    # res = map(lambda x: [int(j) for j in x], res)
    return list(res)


def print_input(data):
    "data print function"
    print(f"DATA:\n{data}\n")


def find_digits(bank):

    m1 = max(bank[:-1])
    idx_m1 = bank[:-1].index(m1)
    m2 = max(bank[idx_m1 + 1:])
    return int(m1 + m2)


def find_digits2(bank, nr, lev=0):

    #print(" " * lev, bank, nr)

    if -nr + 1 == 0:
        return max(bank)

    m = max(bank[:-nr+1])
    idx_m = bank[:-nr+1].index(m)
    res = m + find_digits2(bank[idx_m + 1:], nr-1, lev+1)
    return res



@timeit
def sol01(data):
    "solution for part 1"

    res = []

    for b in data:
        res.append(find_digits(b))

    return sum(res)


@timeit
def sol02(data):
    "solution for part 2"
    res = []

    for b in data:
        #print("")
        tmp = int(find_digits2(b, 12))
        #print(tmp)
        res.append(tmp)

    return sum(res)


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
