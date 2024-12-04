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

    data = "\n".join(data)
    print(f"DATA:\n{data}\n")


def apply_mask(x, y, mask):
    return [(x+dx, y+dy) for dx, dy in mask]


def get_chars(chars, data):
    res = []
    for x, y in chars:
        if -1 < x < len(data[0]) and -1 < y < len(data):
            res.append(data[y][x])
        else:
            return []
    return res


def all_words(x, y, data):

    masks = [
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(0, 0), (1, 1), (2, 2), (3, 3)],
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (-1, 1), (-2, 2), (-3, 3)],
        [(0, 0), (-1, 0), (-2, 0), (-3, 0)],
        [(0, 0), (-1, -1), (-2, -2), (-3, -3)],
        [(0, 0), (0, -1), (0, -2), (0, -3)],
        [(0, 0), (1, -1), (2, -2), (3, -3)]
        ]

    chars = [apply_mask(x, y, m) for m in masks]
    chars = [get_chars(cs, data) for cs in chars]
    chars = ["".join(c) for c in chars if c]
    return chars


@timeit
def sol01(data):
    "solution for part 1"

    res = 0
    for x in range(0, len(data[0])):
        for y in range(0, len(data)):
            tmp = all_words(x, y, data)
            res += tmp.count("XMAS")

    return res


#@timeit
#def sol02(data):
#    "solution for part 2"
#
#    def check_x(x, y, data):
#        masks = {
#            (0, 0): "M",
#            (2, 0): "S",
#            (1, 1): "A",
#            (0, 2): "M",
#            (2, 2): "S"
#            }
#
#        for (dx, dy), c in masks.items():
#            nx = x + dx
#            ny = y + dy
#            if -1 < nx < len(data[0]) and -1 < ny < len(data):
#                if data[ny][nx] != c:
#                    return False
#            else:
#                return False
#
#        return True
#
#    res = 0
#    for y in range(len(data)):
#        for x in range(len(data[0])):
#            if check_x(x, y, data):
#                res += 1
#
#    return res


@timeit
def sol02(data):
    "solution for part 2"

    def check_x(x, y, data):

        masks = [
            [(0, 0), (1, 1), (2, 2)],
            [(2, 0), (1, 1), (0, 2)],
            ]

        chars = [apply_mask(x, y, m) for m in masks]
        chars = ["".join(get_chars(cs, data)) for cs in chars]
        chars = filter(lambda x: x == "MAS" or x == "SAM", chars)
        return len(list(chars)) == 2

    res = 0
    for y in range(len(data)-2):
        for x in range(len(data[0])-2):
            if check_x(x, y, data):
                res += 1

    return res


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
