#!/usr/bin/python


import sys
import copy


cmap = {
        "(" : ")",
        "[" : "]",
        "{" : "}",
        "<" : ">",
}


def parse_input(text):

    res = None
    lines = [ x for x in text.split("\n") if x != "" ]
    res = lines
    return res


def check_syntax(seq):

    stack = []
    res = None

    for c in seq:

        if c in cmap.keys():
            stack.append(c)

        else:
            nc = stack.pop()
            if c != cmap[nc]:
                res = c
                break

    return res, stack


def sol01(lines):

    pts01 = {
        ")" : 3,
        "]" : 57,
        "}" : 1197,
        ">" : 25137,
    }

    res = []
    for l in lines:
        res.append(check_syntax(l)[0])

    res = [ pts01[x] for x in res if x is not None ]
    res = sum(res)
    return res


def comp_score(seq):

    pts02 = {
            ")" : 1,
            "]" : 2,
            "}" : 3,
            ">" : 4,
        }

    res = 0
    for s in seq:
        res = res * 5 + pts02[s]

    return res


def sol02(lines):

    res = []

    for l in lines:
        tmp = check_syntax(l)
        if tmp[0] is None:

            comp = "".join([ cmap[x] for x in tmp[1][::-1] ])
            score = comp_score(comp)
            res.append(score)

            #print("")
            #print(f"text: {l}")
            #print(f"comp: {comp}")
            #print(f"score: {score}")

    res.sort()
    res = res[len(res) // 2]

    return res


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)

    RES = sol01(DATA)
    print("sol01 : {}".format(RES))

    RES = sol02(DATA)
    print("sol02 : {}".format(RES))
