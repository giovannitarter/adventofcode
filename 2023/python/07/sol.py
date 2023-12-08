#!/usr/bin/python


import sys
import copy
import math

tuple_value = {
    (5,) : 7,
    (4, 1) : 6,
    (3, 2) : 5,
    (3, 1, 1) : 4,
    (2, 2, 1) : 3,
    (2, 1, 1, 1) : 2,
    (1, 1, 1, 1, 1) : 1,
}

rs = {s:i for i, s in enumerate(list("AKQJT98765432")[::-1])}
rs_j = {s:i for i, s in enumerate(list("AKQT98765432J")[::-1])}

def parse_input(text):

    res = None
    lines = [x.split() for x in text.split("\n") if x != ""]
    res = [(h, int(bid)) for h, bid in lines]
    return res


def count(hand):

    res = {}
    for c in hand:
        tmp = res.get(c, 0)
        tmp += 1
        res[c] = tmp
    return res


def compare(hand):

    hand, bid = hand

    hand_val = sum([rs[s] * math.pow(len(rs), i) for i, s in enumerate(hand[::-1])])

    cnt = [b for a, b in count(hand).items()]
    cnt.sort(reverse=True)
    cnt = tuple_value[tuple(cnt)]
    hand_val += cnt * math.pow(len(rs), len(hand)+1)

    return hand_val


def countj(hand):

    res = {}
    for c in hand:
        tmp = res.get(c, 0)
        tmp += 1
        res[c] = tmp

    if "J" in res and res["J"] != 5:
        j_nr = res.pop("J")
        max_s, max_count = sorted(res.items(), key=lambda x: x[1])[-1]
        res[max_s] = max_count + j_nr

    return res


def comparej(hand):

    hand, bid = hand

    hand_val = sum([rs_j[s] * math.pow(len(rs_j), i) for i, s in enumerate(hand[::-1])])

    cnt = [b for a, b in countj(hand).items()]
    cnt.sort(reverse=True)
    cnt = tuple_value[tuple(cnt)]
    hand_val += cnt * math.pow(len(rs_j), len(hand)+1)

    return hand_val


def sol01(data):

    data = sorted(data, key=compare)
    return sum([d[1] * (i+1) for i, d in enumerate(data)])


def sol02(data):
    data = sorted(data, key=comparej)
    return sum([d[1] * (i+1) for i, d in enumerate(data)])


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)
    print(f"DATA:\n{DATA}\n")

    SOL01 = sol01(DATA)
    print("SOL01: {}".format(SOL01))

    SOL02 = sol02(DATA)
    print("SOL02: {}".format(SOL02))

