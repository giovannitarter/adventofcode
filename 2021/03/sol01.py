#!/usr/bin/python


import sys


def transpose(mat):
    return [ list(x) for x in zip(*mat) ]


def to_int(chars):

    res = "".join(chars)
    res = int(res, base=2)
    return res


if __name__ == "__main__":

    RES01 = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    LINES = [ list(x) for x in TEXT.split("\n") if x != "" ]

    gamma = []
    epsilon = []
    for l in transpose(LINES):
        zeros = l.count("0")
        ones = l.count("1")

        if zeros > ones:
            gamma.append("0")
            epsilon.append("1")
        else:
            gamma.append("1")
            epsilon.append("0")

    gamma = to_int(gamma)
    epsilon = to_int(epsilon)

    print("gamma: {}".format(gamma))
    print("epsilon: {}".format(epsilon))

    RES01 = epsilon * gamma
    print("res01 : {}".format(RES01))
