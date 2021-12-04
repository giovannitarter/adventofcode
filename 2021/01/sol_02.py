#!/usr/bin/python


import sys



def sol01(lines):

    res = 0
    for i in range(1, len(lines)):
        if (lines[i] - lines[i-1] > 0):
            res = res + 1

    return res


def sol02(lines):

    res = 0
    mob_sum = sum(lines[0:3])

    for i in range(1, len(lines) - 2):
        new = mob_sum - lines[i-1] + lines[i + 2]
        if new > mob_sum:
            res = res + 1
    return res


if __name__ == "__main__":

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    LINES = [ int(x) for x in TEXT.split("\n") if x != "" ]


    res = sol01(LINES)
    print("res01 : {}".format(res))

    res = sol02(LINES)
    print("res02 : {}".format(res))
