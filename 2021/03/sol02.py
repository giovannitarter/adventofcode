#!/usr/bin/python


import sys
import copy


def transpose(mat):
    return [ list(x) for x in zip(*mat) ]


def to_int(chars):

    res = "".join(chars)
    res = int(res, base=2)
    return res


def bit_criteria(pos, mat, tp):

    tmp = transpose(mat)

    zeros = tmp[pos].count("0")
    ones = tmp[pos].count("1")

    if tp == "ox":
        res = "1"
        if zeros > ones:
            res = "0"

    elif tp == "co2":
        res = "0"
        if zeros > ones:
            res = "1"

    return res


def find_value(mat, tp):

    res = copy.deepcopy(mat)
    rowlen = len(res[0])

    for i in range(0, rowlen):

        #print("iteration i: {}".format(i))

        cbit = bit_criteria(i, res, tp)

        tmp = []
        for row in res:
            if row[i] == cbit:
                tmp.append(row)

        res = tmp
        if len(tmp) == 1:
            res = res[0]
            break

    print(res)
    return res




if __name__ == "__main__":

    RES02 = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    LINES = [ list(x) for x in TEXT.split("\n") if x != "" ]


    ox = find_value(LINES, "ox")
    ox = to_int(ox)
    print(ox)

    co2 = find_value(LINES, "co2")
    co2 = to_int(co2)
    print(co2)

    RES02 = co2 * ox

    print("res02 : {}".format(RES02))
