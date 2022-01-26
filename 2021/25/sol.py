#!/usr/bin/python


import sys


def parse_input(text):

    res = None
    lines = [x for x in text.split("\n") if x != ""]
    res = [list(l) for l in lines]
    return res


def copy_mat(mat):

    res = []
    for y in range(len(mat)):
        res.append(list(mat[y]))
    return res


def print_mat(mat):

    for r in mat:
        print("".join(r))
    return


def step(data):

    max_x = len(data[0])
    max_y = len(data)

    res = copy_mat(data)

    for y, row in enumerate(data):
        for x, val in enumerate(row):

            if val == ">":
                nxt = (x+1) % max_x
                if data[y][nxt] == ".":
                    res[y][x] = "."
                    res[y][nxt] = ">"

    res2 = copy_mat(res)

    for y, row in enumerate(res):
        for x, val in enumerate(row):
            if val == "v":
                nxt = (y+1) % max_y
                if res[nxt][x] == ".":
                    res2[y][x] = "."
                    res2[nxt][x] = "v"

    return res2


def mat_eq(m1, m2):

    txt1 = "".join(["".join(x) for x in m1])
    txt2 = "".join(["".join(x) for x in m2])
    res = (txt1 == txt2)
    return res



if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)

    #print_mat(DATA)

    i = 0
    while True:
        RES = step(DATA)
        i += 1

        if mat_eq(RES, DATA):
            break

        DATA = RES

    RES = i

    print("sol01: {}".format(RES))
