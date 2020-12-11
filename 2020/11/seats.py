#!/usr/bin/python

import sys


fd = open(sys.argv[1])
text = fd.read()
fd.close()


lines = text.split("\n")
lines = [l for l in lines if l != ""]

mat = []
for l in lines:
    mat.append(list(l))


def print_mat(mat):
    print("\n====================")
    for i in mat:
        print(i)
    print("====================")


def replace_mat(mat, x, y, c):
    mat[y].pop(x)
    mat[y].insert(x, c)
    return


def neighbors(mat, x, y):
    
    max_x = len(mat[0])
    max_y = len(mat)

    res = []
    range_y = range(y-1, y+1)
    range_y = [ y for y in range_y if (y >= 0 and y <= max_y)]
    range_x = range(x-1, x+1)
    range_x = [ x for x in range_x if (x >= 0 and x <= max_x)]


    for y in range_y:
        for x in range_x:
            res.append((x,y))

    res.remove((x,y))

    return res


def step(mat):

    new_mat = len(mat) * [len(mat[0]) * [" "]]
    print_mat(new_mat)

    for x in range(0, len(mat[0])):
        for y in range(0, len(mat)):
            
            print("aa,", x, y, mat[y][x])

            if mat[y][x] == ".":
                continue

            elif mat[y][x] == "L":
                for xn, yn in neighbors(mat, x, y):
                    if mat[yn][xn] != ".":
                        replace_mat(new_mat, xn, yn, "#")
    return new_mat



print_mat(mat)
#replace_mat(mat, 0, 9, "#")
mat = step(mat)
#print(neighbors(mat, 9, 9))
print_mat(mat)

