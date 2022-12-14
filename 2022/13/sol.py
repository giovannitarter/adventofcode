#!/usr/bin/python


import sys
import copy
import functools



def parse_input(text):
    res = [tuple(x.strip().split("\n")) for x in text.split("\n\n") if x != ""]
    res = [(eval(l), eval(r)) for l, r in res]
    return res


def compare(l, r):

    #print(f"Compare {l} vs {r}")

    if isinstance(l, int) and isinstance(r, int):

        if l == r:
            return 0
        elif l > r:
            return 1
        else:
            return -1

    elif isinstance(l, list) and isinstance(r, int):
        return compare(l, [r])

    elif isinstance(l, int) and isinstance(r, list):
        return compare([l], r)

    elif isinstance(l, list) and isinstance(r, list):

        if l and not r:
            return 1
        elif not l and r:
            return -1
        elif not l and not r:
            return 0

        res = compare(l[0], r[0])
        if res == 0:
            return compare(l[1:], r[1:])
        else:
            return res


def sol01(data):

    data = copy.deepcopy(data)

    res = 0
    for idx, (l, r) in enumerate(data):
        idx += 1
        if compare(l, r) == -1:
            res += idx
    return res


def sol02(data):

    pkgs = []
    for d in data:
        l, r = d
        pkgs.append(l)
        pkgs.append(r)

    divider = ["[[2]]", "[[6]]"]
    divider = [eval(x) for x in divider]
    pkgs.extend(divider)

    pkgs = sorted(pkgs, key=functools.cmp_to_key(compare))

    res = 1
    for idx, p in enumerate(pkgs):
        for d in divider:
            if compare(p, d) == 0:
                res *= idx + 1

    return res


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)

    SOL01 = sol01(DATA)
    print("SOL01: {}".format(SOL01))

    SOL02 = sol02(DATA)
    print("SOL02: {}".format(SOL02))

