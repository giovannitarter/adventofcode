#!/usr/bin/python


import sys
import copy
import re


class Maps():

    def __init__(self, ranges):


        self.ranges = []
        for l in ranges:
            d, s, r = [int(x) for x in l.split(" ")]
            self.ranges.append((s, s+r, d-s))
            self.ranges.sort()

        #self.ranges = [[(int(s), int(s) + int(r), int(d) - int(s)) for d, s, r in l.split()] for l in ranges]
        #print(self.ranges)

    def get(self, v):
        for s, e, d in self.ranges:
            if v >= s and v < e:
                return v + d
        return v


def parse_input(text):

    res = None

    seeds = []
    maps = {}

    for chunk in text.split("\n\n"):
        chunk = chunk.strip()

        if chunk.startswith("seeds: "):
            chunk = chunk.replace("seeds: ", "")
            seeds = [int(x) for x in chunk.split(" ")]

        else:
            lines = chunk.split("\n")
            m = re.match(r"([a-z]*)-to-([a-z]*) map:", lines[0])
            src = m.group(1)
            dst = m.group(2)

            maps[src] = (dst, Maps(lines[1:]))

    return seeds, maps


def apply_map(seed_range, map):

    #print(f"seed ranges: {seed_range}")
    #print(f"map ranges: {map.ranges}")

    res = []
    while seed_range:

        s, e = seed_range.pop(0)

        #print(f"working on range: {s} - {e}")

        range_find = False

        for rs, re, d in map.ranges:

            if s >= rs and e < re:
                res.append((s+d, e+d))
                range_find = True
                break

            elif(s <= rs and rs < e and e < re):
                seed_range.append((s, rs))
                res.append((rs+d, e+d))
                range_find = True
                break

            elif(rs < s and re > s and re <= e ):
                res.append((s+d, re+d))
                seed_range.append((re, e))
                range_find = True
                break

            elif(s <= rs and re < e):
                res.append((rs+d, re+d))
                seed_range.append((s, rs))
                seed_range.append((re, e))
                range_find = True
                break

        if range_find == False:
            res.append((s, e))


    return res




def sol01(data):
    res = None

    res = []
    seeds, maps = data
    for s in seeds:
        pos = "seed"
        while pos != "location":
            pos, map = maps[pos]
            s = map.get(s)
        res.append(s)

    res = min(res)
    return res


def sol02(data):

    res = 0
    seeds, maps = data

    ranges = []
    for i in range(0, len(seeds), 2):
        ranges.append((seeds[i], seeds[i] + seeds[i+1]))

    ranges = sorted(ranges)
    #print(ranges)

    pos = "seed"
    tot_sum = sum([y-x for x, y in ranges])
    #print(f"pos: {pos} -> {ranges}")

    while pos != "location":
        #print(f"\n")
        csum = sum([y-x for x, y in ranges])

        if csum != tot_sum:
            print("Error")
            sys.exit(1)

        pos, map = maps[pos]
        ranges = apply_map(ranges, map)
        #print(f"pos: {pos} -> {ranges}")

    res = min([x for x, y in ranges])

    return res


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

    #too low:   22504597
    #too high: 102900316
    #           79004094