#!/usr/bin/python
"""
solution file
"""

import sys
import re
import functools


def parse_input(text):
    "input parsing function"
    return text.replace("\n", "")


def print_input(data):
    "data print function"
    print(f"DATA:\n{data}\n")


def sol01(data):
    "solution for part 1"
    cmds = re.findall(r"mul\(\d+,\d+\)", data)
    cmds = [x[4:-1].split(",") for x in cmds]
    prods = [int(a) * int(b) for a, b in cmds]
    return sum(prods)


#def sol02(data):
#    "solution for part 2"
#
#    cmds = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data)
#
#    en = True
#    prod = 0
#    for c in cmds:
#        if c == "do()":
#            en = True
#        elif c == "don't()":
#            en = False
#        elif c.startswith("mul") and en:
#            factors = c[4:-1].split(",")
#            prod += int(factors[0]) * int(factors[1])
#
#    return prod


def sol02(data):
    "solution for part 2"

    def func(acc, c):

        en, res = acc
        if c == "do()":
            return (True, res)
        elif c == "don't()":
            return (False, res)
        elif c.startswith("mul"):
            if en:
                factors = c[4:-1].split(",")
                return (en, res + int(factors[0]) * int(factors[1]))
            else:
                return (en, res)

    cmds = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data)
    return functools.reduce(func, cmds, (True, 0))[1]


if __name__ == "__main__":

    RES = None

    with open(sys.argv[1], encoding="utf8") as fd:
        TEXT = fd.read()

    DATA = parse_input(TEXT)
    print_input(DATA)

    SOL01 = sol01(DATA)
    print(f"SOL01: {SOL01}")

    SOL02 = sol02(DATA)
    print(f"SOL02: {SOL02}")
