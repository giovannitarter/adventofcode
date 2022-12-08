#!/usr/bin/python

import sys
from collections import deque


def parse_input(text):
    return [x for x in text.split("\n") if x != ""]


def sol(data, seq_len):
    res = None

    last_seen = deque(data[0:seq_len])

    for i in range(seq_len, len(data)):

        if len(set(last_seen)) == seq_len:
            res = i
            break

        last_seen.popleft()
        last_seen.append(data[i])

    return res


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)

    #for d in DATA:
    #    res = sol01(d)
    #    print(f"{d} -> {res}")
    #print(f"DATA:\n{DATA}\n")

    SOL01 = sol(DATA[0], 4)
    print("SOL01: {}".format(SOL01))

    SOL02 = sol(DATA[0], 14)
    print("SOL02: {}".format(SOL02))

