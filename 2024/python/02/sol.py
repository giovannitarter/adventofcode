#!/usr/bin/python
"""
solution file
"""

import sys
import copy


def parse_input(text):
    "input parsing function"
    return [list(map(int, x.split())) for x in text.split("\n") if x != ""]


def print_input(data):
    "data print function"
    print(f"DATA:\n{data}\n")


def is_safe(levels):
    diffs = [b-a for a, b in zip(levels, levels[1:])]
    in_interval = [1 <= abs(d) <= 3 for d in diffs]
    return all(in_interval) and (all(map(lambda x: x < 0, diffs)) or all(map(lambda x: x > 0, diffs)))


def is_safe2(levels):

    if is_safe(levels):
        return True
    else:
        diffs = [b-a for a, b in zip(levels, levels[1:])]

        dec = [x < 0 for x in diffs]
        if dec.count(False) == 1:
            tmp = list(levels)
            tmp.pop(dec.index(False))
            if is_safe(tmp):
                return True

            tmp = list(levels)
            tmp.pop(dec.index(False) + 1)
            if is_safe(tmp):
                return True

        inc = [x > 0 for x in diffs]
        if inc.count(False) == 1:
            tmp = list(levels)
            tmp.pop(inc.index(False))
            if is_safe(tmp):
                return True

            tmp = list(levels)
            tmp.pop(inc.index(False) + 1)
            if is_safe(tmp):
                return True

        in_interval = [1 <= abs(d) <= 3 for d in diffs]
        if not all(in_interval):
            tmp = list(levels)
            tmp.pop(in_interval.index(False))
            if is_safe(tmp):
                return True

            tmp = list(levels)
            tmp.pop(in_interval.index(False)+1)
            if is_safe(tmp):
                return True



    return False



def sol01(data):
    "solution for part 1"
    return len(list(filter(is_safe, data)))


#def sol02(data):
#    "solution for part 2"
#
#    cnt = 0
#    for d in data:
#        if is_safe(d):
#            cnt += 1
#        else:
#            for idx, e in enumerate(d):
#                tmp = list(d)
#                tmp.pop(idx)
#                if is_safe(tmp):
#                    cnt += 1
#                    break
#    return cnt


def sol02(data):
    "solution for part 2"
    return len(list(filter(is_safe2, data)))



if __name__ == "__main__":

    RES = None

    with open(sys.argv[1], encoding="utf8") as fd:
        TEXT = fd.read()

    DATA = parse_input(TEXT)
    #print_input(DATA)

    SOL01 = sol01(DATA)
    print(f"SOL01: {SOL01}")

    SOL02 = sol02(DATA)
    print(f"SOL02: {SOL02}")
