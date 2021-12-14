#!/usr/bin/python


import sys
import copy



def parse_input(text):

    res = None
    lines = [ x for x in text.split("\n") if x != "" ]

    dots = []
    folds = []
    max_x = 0
    max_y = 0

    for l in lines:

        if not l.startswith("fold"):

            x, y= [ int(coord) for coord in l.split(",") ]

            if x > max_x:
                max_x = x

            if y > max_y:
                max_y = y

            dots.append((x,y))

        else:
            ax, val = l[11:].split("=")
            folds.append((ax, int(val)))

    mat = [ list((max_x + 1) * ".") for x in range (max_y + 1) ]
    for x, y in dots:
        mat[y][x] = "#"

    return mat, folds


def fold_horiz(mat, fold_y):

    new_rows = fold_y
    new_cols = len(mat[0])

    new_mat = mat[:fold_y]
    bot_mat = mat[fold_y:]

    for y, new_row in enumerate(new_mat):
        for x, val in enumerate(new_row):

            if bot_mat[fold_y - y][x] == "#":
                new_mat[y][x] = "#"

    return(new_mat)


def fold_vert(mat, fold_x):

    new_rows = len(mat)
    new_cols = fold_x

    lt_mat = [ r[:fold_x] for r in mat ]
    rt_mat = [ r[fold_x:] for r in mat ]

    for y, row in enumerate(rt_mat):
        for x, val in enumerate(row):

            if rt_mat[y][x] == "#":
                lt_mat[y][fold_x - x] = "#"

    return lt_mat


def count_dots(mat):

    res = []
    for row in mat:
        res.append(row.count("#"))

    res = sum(res)
    return res


def print_sheet(sheet):

    print("")
    for l in sheet:
        print("".join(l))

    return


def apply_fold(sheet, fold):

    f, val = fold

    if f == "x":
        sheet = fold_vert(sheet, val)
    elif f == "y":
        sheet = fold_horiz(sheet, val)

    return sheet


def sol01(sheet, folds):
    sheet = apply_fold(sheet, folds.pop(0))
    return sheet


def sol02(sheet, folds):

    for f in folds:
        sheet = apply_fold(sheet, f)

    print_sheet(sheet)
    return


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    SHEET, FOLDS = parse_input(TEXT)

    print(f"FOLDS: {FOLDS}")

    SHEET = sol01(SHEET, FOLDS)
    RES = count_dots(SHEET)

    print("")
    print("res01 : {}".format(RES))

    print("res02:")
    sol02(SHEET, FOLDS)
