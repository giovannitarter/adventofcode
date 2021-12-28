#!/usr/bin/python


import sys
import copy
import re


class DiceD():

    def __init__(self):
        self.val = 0
        self.max = 100

    def cast(self):

        res = []
        for i in range(3):
            res.append(1 + self.val)
            self.val = (self.val + 1) % self.max
        return sum(res)


def three_dirac_throws():

    res = {}

    for a in range(1, 4):
        for b in range(1, 4):
            for c in range (1, 4):

                s = sum([a, b, c])
                tmp = res.get(s, 0)
                tmp += 1
                res[s] = tmp
    
    return res


def dirac_dice(will_play, pos1, pos2, scor1, scor2, tdt):

    if scor1 >= 21:
        return (1, 0)

    elif scor2 >= 21:
        return (0, 1)

    res1 = 0
    res2 = 0
    
    if will_play == 1:
        for i in TDT:
            new_p = ((pos1-1+i) % 10) + 1
            ns1, ns2 = dirac_dice(2, new_p, pos2, scor1+new_p, scor2, tdt)
            res1 += ns1 * TDT[i] 
            res2 += ns2 * TDT[i]
        res = (res1, res2)
        

    elif will_play == 2:
        for i in TDT:
            new_p = ((pos2-1+i) % 10) + 1
            ns1, ns2 = dirac_dice(1, pos1, new_p, scor1, scor2+new_p, tdt)
            res1 += ns1 * TDT[i]
            res2 += ns2 * TDT[i]
        res = (res1, res2)

    return res



def parse_input(text):

    res = {}
    lines = [ x for x in text.split("\n") if x != "" ]

    for l in lines:
        m = re.match(r"Player (\d*) starting position: (\d*)", l)
        res[int(m[1])] = int(m[2])
    return res


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    PPOS = parse_input(TEXT)
    PPOS2 = dict(PPOS)

    SCORE = {}
    for p in PPOS:
        SCORE[p] = 0

    D = DiceD()

    i = 0
    winner = None
    while not winner:
        #print("")
        for p in sorted(PPOS):
            PPOS[p] = (1 + (PPOS[p] -1 + D.cast()) % 10)
            SCORE[p] = SCORE[p] + PPOS[p]
            i += 3

            if max(SCORE.values()) >= 1000:
                winner = True
                break

            #print(f"player{p}: pos:{PPOS[p]} score:{SCORE[p]}")

    RES = i * min(SCORE.values())
    print("sol01: {}".format(RES))

    TDT = three_dirac_throws()
    RES = dirac_dice(1, PPOS2[1], PPOS2[2], 0, 0, TDT)
    RES = max(*RES)
    print("sol02: {}".format(RES))
