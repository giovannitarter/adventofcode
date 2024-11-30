#!/usr/bin/python


import sys
import copy



def parse_input(text):

    res = [x.split() for x in text.split("\n") if x != ""]
    return [(record, tuple(map(int, count.split(",")))) for record, count in res]


def count_arrangements(record, count, lev=0, cache={}):

    #print(" " * lev, record, count)

    if len(record) == 0:
        if len(count) == 0:
            return 1
        return 0

    if len(count) == 0:
        if "#" in record:
            return 0
        return 1

    if (record, count) in cache:
        return cache[(record, count)]

    res = 0
    if record[0] == ".":
        res += count_arrangements(record[1:], count, lev+1, cache)
    elif record[0] == "#":
        if "." not in record[:count[0]]:
            if count[0] < len(record) and record[count[0]] != "#":
                res += count_arrangements("." + record[count[0]+1:], count[1:], lev+1, cache)
            elif count[0] == len(record):
                res += count_arrangements(record[count[0]:], count[1:], lev+1, cache)
    elif record[0] == "?":
        res += count_arrangements("." + record[1:], count, lev+1, cache)
        res += count_arrangements("#" + record[1:], count, lev+1, cache)

    else:
        print("Error")
        sys.exit(1)

    cache[(record, count)] = res

    return res



def sol01(data):
    return sum(count_arrangements(r, c) for r, c in data)


def sol02(data):
    data = [("?".join([r] * 5), c * 5) for r, c in data]
    return sum(count_arrangements(r, c, 0, {}) for r, c in data)


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)
    #print(f"DATA:\n{DATA}\n")

    SOL01 = sol01(DATA)
    print("SOL01: {}".format(SOL01))

    SOL02 = sol02(DATA)
    print("SOL02: {}".format(SOL02))

