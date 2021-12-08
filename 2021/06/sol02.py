#!/usr/bin/python


import sys
import copy

def step(freq):

    reproducing = freq.pop(0)
    freq[6] = freq[6] + reproducing
    freq.append(reproducing)
    return freq


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    LINES = [ x for x in TEXT.split("\n") if x != "" ]
    FISHES = [ int(x) for x in LINES[0].split(",") ]

    FREQ = []
    for i in range(9):
        FREQ.append(FISHES.count(i))

    print(FREQ)
    for i in range(256):

        print("\nday {}".format(i))
        print("sum: {}".format(sum(FREQ)))
        print(FREQ)

        FREQ = step(FREQ)

    RES = sum(FREQ)
    print("res: {}".format(RES))
