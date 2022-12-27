#!/usr/bin/python


import sys
import copy
import re
import itertools


class Valve:

    def __init__(self, name, flow, neigh):
        self.name = name
        self.flow = int(flow)
        self.neigh = neigh.split(", ")
        return

    def __repr__(self):
        return f"Valve {self.name}, flow: {self.flow}, neigh: {self.neigh}"


def parse_input(text):

    lines = [x for x in text.split("\n") if x != ""]
    res = [re.match(r"Valve ([A-Z]*) has flow rate=(\d*); tunnels* leads* to valves* ([A-Z, ]*)", l) for l in lines]
    res = [r.groups() for r in res if r is not None]
    res = [Valve(*r) for r in res]

    valves = {}
    for r in res:
        valves[r.name] = r

    return valves


def visit(s, data):

    visited = set()
    visited.add(s)
    q = [s]
    parent = {}

    while q:
        v = data[q.pop(0)]
        for n in v.neigh:
            if n not in visited:
                visited.add(n)
                q.append(n)
                parent[n] = v.name

    paths = {}
    for d in data:
        tmp = []
        v = d
        while v != s:
            tmp.append(v)
            v = parent[v]

        tmp.reverse()
        paths[d] = tmp

    return paths


def all_paths(data):

    #res = {}
    plen = {}
    for s in data:
        tmp = visit(s, data)
        for d in tmp:
            #res[(s, d)] = tmp[d]
            plen[(s, d)] = len(tmp[d])

    #return plen, res
    return plen


def max_flow(plen, valves, vcand, cv, time, max_time, opened, lev=0):

    ind = " " * lev
    #print(f"{ind}mf - curr:{cv}, time:{time: 2}, {opened}")

    #neigh = neighbors(cv, vcand, opened)
    neigh = [c for c in vcand if c != cv and c not in opened]

    res = 0
    if not neigh or time > max_time:
        for o in opened:
            if opened[o] <= max_time:
                res += valves[o].flow * (max_time - opened[o])

        #print(f"{ind}return {opened}")
        return res

    tmp = []
    for n in neigh:
        w_opened = dict(opened)
        otime = time + plen[(cv, n)] + 1
        w_opened[n] = otime
        tmp.append(max_flow(plen, valves, vcand, n, otime, max_time, w_opened, lev=lev+1))

    res = max(tmp)

    #print(f"{ind}return max {tmp}")
    return res


def sol01(data):
    plen = all_paths(data)
    vcand = [d for d in data if data[d].flow > 0]
    res = max_flow(plen, data, vcand, "AA", 0, 30, {})
    return res


def sol02(data):

    res = 0

    plen = all_paths(data)

    vcand = [d for d in data if data[d].flow > 0]
    vcand = set(vcand)

    k = 2
    min_perm = len(vcand) - k
    max_perm = len(vcand) + k

    #for i in range(min_perm, max_perm):
    it = 0
    for i in [len(vcand)//2]:

        for cmb in itertools.combinations(vcand, i):
            vcnd1 = list(cmb)
            vcnd2 = list(vcand.difference(vcnd1))

            res1 = max_flow(plen, data, vcnd1, "AA", 0, 26, {})
            res2 = max_flow(plen, data, vcnd2, "AA", 0, 26, {})
            tmp = res1 + res2

            if tmp > res:
                res = tmp

            print(f"{it: 4} - {tmp}")

            it += 1

    return res


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)
    for d in DATA:
        print(DATA[d])

    SOL01 = sol01(DATA)
    print("SOL01: {}".format(SOL01))

    SOL02 = sol02(DATA)
    print("SOL02: {}".format(SOL02))

