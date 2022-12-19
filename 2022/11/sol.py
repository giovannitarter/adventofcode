#!/usr/bin/python


import sys
import copy
import re


class Monkey():

    def __init__(self, desc):
        ml = [x.strip() for x in desc.split("\n")]
        self.nr = int(ml[0][-2])
        self.items = [int(x) for x in re.sub(r".*: ", "", ml[1]).split(", ")]
        self.op = re.sub(r".*new = ", "", ml[2])
        self.test = int(re.sub(r".*by ", "", ml[3]))
        self.true = int(re.sub(r".*monkey ", "", ml[4]))
        self.false = int(re.sub(r".*monkey ", "", ml[5]))
        return


    def __repr__(self):

        res = []
        res.append(f"Monkey {self.nr}: {self.items}")
        return "\n".join(res)


def parse_input(text):
    res = [Monkey(x) for x in text.split("\n\n") if x != ""]
    return res


def print_game(data):
    for d in data:
        print(d)
    return


def game_round(data):

    res = {}
    for m in data:
        res[m.nr] = len(m.items)
        while m.items:
            old = m.items.pop(0)
            new = eval(m.op)
            new = new // 3
            if new % m.test == 0:
                data[m.true].items.append(new)
            else:
                data[m.false].items.append(new)

    return res


def sol01(data):

    data = copy.deepcopy(data)

    res = [0 for _ in range(len(data))]
    for r in range(1, 21, 1):
        cnt = game_round(data)

        for c in cnt:
            res[c] = res[c] + cnt[c]

    res = sorted(res, reverse=True)[:2]
    res = res[0] * res[1]
    return res


def game_round2(data):

    mcm = 1
    for d in data:
        mcm *= d.test

    res = {}
    for m in data:
        res[m.nr] = len(m.items)

        while m.items:
            old = m.items.pop(0)
            new = eval(m.op)
            new = new % mcm
            if new % m.test == 0:
                data[m.true].items.append(new)
            else:
                data[m.false].items.append(new)

    return res


def sol02(data):

    data = copy.deepcopy(data)
    for m in data:
        tmp = []
        for i in m.items:
            tmp.append(i)
        m.items = tmp

    #print_game(data)
    res = [0 for _ in range(len(data))]
    for r in range(1, 10001, 1):
        cnt = game_round2(data)

        for c in cnt:
            res[c] = res[c] + cnt[c]

    res = sorted(res, reverse=True)[:2]
    res = res[0] * res[1]
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

