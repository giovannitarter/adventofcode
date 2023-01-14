#!/usr/bin/python


import sys
import copy
import re



class Symbol():

    def __init__(self, m, c):
        self.m = m
        self.c = c

    #Assuming humn is the only variable and it IS a TREE
    # humn cannot be used on the left side of more than 1 other variable
    def __add__(self, other):
        return Symbol(self.m + other.m, self.c + other.c)

    def __sub__(self, other):
        return Symbol(self.m - other.m, self.c - other.c)

    def __mul__(self, other):
        return Symbol(
                self.m * other.c + self.c * other.m,
                self.c * other.c
                )

    #Assuming humn will be never at the denominator
    def __truediv__(self, other):
        self.m /= other.c
        self.c /= other.c
        return self

    def __repr__(self):
        return f"{self.m} * humn + {self.c}"


def parse_input(text):

    res = {}
    for l in [x for x in text.split("\n") if x != ""]:

        m = re.match(r"(\w+): (\d+)", l)
        if m:
            res[m.group(1)] = int(m.group(2))

        m = re.match(r"(\w+): (\w+) (.) (\w+)", l)
        if m:
            res[m.group(1)] = tuple(m.groups()[1:])

    return res


def solve(node, env):

    if isinstance(env[node], int):
        return env[node]

    else:
        a, op, b = env[node]
        a = solve(a, env)
        b = solve(b, env)

        text = f"{a} {op} {b}"
        return int(eval(text))


def solve2(node, env):

    if node == "humn":
        return Symbol(1, 0)

    elif isinstance(env[node], int):
        return Symbol(0, env[node])

    else:
        a, op, b = env[node]
        a = solve2(a, env)
        b = solve2(b, env)
        text = f"a {op} b"
        return eval(f"a {op} b")


def sol01(data):
    res = solve("root", data)
    return res


def sol02(data):
    work = copy.copy(data)
    new_root = (work["root"][0], "-", work["root"][2])
    work["root"] = new_root
    res = solve2("root", work)
    res = int(- res.c / res.m)
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

