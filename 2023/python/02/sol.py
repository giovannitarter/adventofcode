#!/usr/bin/python


import sys
import copy
import re


class Draw:

    def __init__(self, l):
        
        if isinstance(l, str):
            self.cubes = {}
            for c in l.split(", "):
                cm = re.match(r"(\d*) (red|green|blue)", c)
                self.cubes[cm.group(2)] = int(cm.group(1))
        elif isinstance(l, dict):
            self.cubes = l
        
        return

    def __repr__(self):
        return(str(self.cubes))

    def __le__(self, other):

        for k in self.cubes:
            ov = other.cubes.get(k, 0)
            if self.cubes[k] > ov:
                return False
        
        return True


    def min_cubes(self, other):

        res = {}
        for k in ("red", "green", "blue"):
            sv = self.cubes.get(k, 0)
            ov = other.cubes.get(k, 0)
            res[k] = max(sv, ov)

        return Draw(res)


    def power(self):
        
        res = 1
        for k in ("red", "green", "blue"):
            res *= self.cubes.get(k, 0)

        return res



def parse_line(l):

    match = re.match(r"Game (\d*): ", l)
    game_id = int(match.group(1))
    draws = [Draw(x) for x in l[match.end():].split("; ")]    
    
    return (game_id, draws)


def parse_input(text):

    lines = [x for x in text.split("\n") if x != ""]
    res = [parse_line(l) for l in lines]
    return res


def sol01(data):

    cmp = "12 red, 13 green, 14 blue"
    cmp = Draw(cmp)

    #res = sum([id for id, draws in data if all([d <= cmp for d in draws])])

    res = 0
    for id, draws in data:
        test = [d <= cmp for d in draws]
        if all(test):
            res += id

    return res


def sol02(data):
    
    res = 0
    for id, draws in data:
        cmp = "0 red, 0 green, 0 blue"
        cmp = Draw(cmp)
        for d in draws:
            cmp = d.min_cubes(cmp)
        res += cmp.power()

    return res


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)
    #print(f"DATA:\n{DATA}\n")

    SOL01 = sol01(DATA)
    print("SOL01: {}".format(SOL01))
    
    SOL02 = sol02(DATA)
    print("SOL02: {}".format(SOL02))

