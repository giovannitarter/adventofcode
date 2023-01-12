#!/usr/bin/python


import sys
import copy



def parse_input(text):

    tmp = {}
    res = []
    for x in text.split("\n"):
        if x != "":
            val = int(x)

            nr = tmp.get(val, -1)
            nr += 1
            tmp[val] = nr

            res.append((val, nr))

    return res


def shift_sol(val, data):

    pos = data.index(val)
    val, nr = val

    while val != 0:

        if val > 0:
            n_pos = (pos + 1) % len(data)
            tmp = data[n_pos]
            data[n_pos] = data[pos]
            data[pos] = tmp
            val -= 1

        elif val < 0:
            n_pos = (pos - 1) % len(data)
            tmp = data[n_pos]
            data[n_pos] = data[pos]
            data[pos] = tmp
            val += 1

        pos = n_pos

    while data[0] != (0, 0):
        data.append(data.pop(0))

    return data


def mod_sol(enc, data):

    val, nr = enc
    if val == 0:
        return data
    cpos = data.index(enc)

    data.pop(cpos)
    ipos = (cpos + val) % (len(data))
    data.insert(ipos, enc)

    return data


def compare_lists(a, b):

    if len(a) != len(b):
        return False

    for i, (x, y) in enumerate(zip(a, b)):
        if x != y :
            return False

    return True


def sol01(data):

    orig = list(data)
    work = list(data)

    for idx, val in enumerate(orig):
        work = mod_sol(val, work)

    res = []
    pos = work.index((0, 0))
    for i in range(1, 4):
        pos += 1000
        res.append(work[pos % len(work)][0])

    res = sum(res)
    return res


def sol02(data):

    orig = [(x * 811589153, nr) for (x, nr) in data]
    work = list(orig)

    for i in range(10):
        for idx, val in enumerate(orig):
            work = mod_sol(val, work)

    res = []
    pos = work.index((0, 0))
    for i in range(1, 4):
        pos += 1000
        res.append(work[pos % len(work)][0])

    res = sum(res)
    return res


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)

    SOL01 = sol01(DATA)
    print("SOL01: {}".format(SOL01))

    SOL02 = sol02(DATA)
    print("SOL02: {}".format(SOL02))

