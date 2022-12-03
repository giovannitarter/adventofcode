#!/usr/bin/python


import sys
import copy



def parse_input(text):
    res = [(set(x[:len(x)//2]), set(x[len(x)//2:])) for x in text.split("\n") if x != ""]
    return res


def priority(t):
    if t >= "a" and t <= "z":
        res = (ord(t) - ord("a") + 1)
    elif t >= "A" and t <= "Z":
        res = (ord(t) - ord("A") + 27)
    return res


def sol01(data):

    comm = []
    for c1, c2 in data:
        comm.append(c1.intersection(c2).pop())

    res = []
    for t in comm:
        res.append(priority(t))
    return sum(res)


def sol02(data):
    
    res = []

    for idx in range(0, len(data), 3):
        
        grp = data[idx:idx+3]
        grp = [c1.union(c2) for c1, c2 in grp]
        
        badge = grp[0]
        for r in grp[1:]:
            badge = badge.intersection(r)

        res.append(priority(badge.pop()))
    
    return sum(res)


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)
    SOL01 = sol01(DATA)
    print("SOL01 : {}".format(SOL01))

    SOL02 = sol02(DATA)
    print("SOL02 : {}".format(SOL02))
    
