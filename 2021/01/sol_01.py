#!/usr/bin/python


import sys



if __name__ == "__main__":

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    LINES = [ int(x) for x in TEXT.split("\n") if x != "" ]

    res = 0
    for i in range(1, len(LINES)):
        if (LINES[i] - LINES[i-1] > 0):
            res = res + 1

    print("res01 : {}".format(res))
