#!/usr/bin/python


import sys
import copy



def parse_input(text):
    res = [list(x) for x in text.split("\n") if x != ""]
    return res


def visible(start, prog, mat):

    res = []
    sx, sy = start
    dx, dy = prog
    x_len = len(mat[0])
    y_len = len(mat)
    
    cx = sx
    cy = sy
    max_h = -1
    while cx >= 0 and cx < x_len and cy >= 0 and cy < y_len:

        #print(f"{cy} {cx}")
        ctree_h = int(mat[cy][cx])
        if ctree_h > max_h:
            max_h = ctree_h
            res.append((cx, cy))
        
        cx = cx + dx
        cy = cy + dy
        
    return res


def visible2(start, prog, mat):

    res = []
    sx, sy = start
    dx, dy = prog
    x_len = len(mat[0])
    y_len = len(mat)
    
    cx = sx + dx
    cy = sy + dy
    vp_h = int(mat[sy][sx])
    while cx >= 0 and cx < x_len and cy >= 0 and cy < y_len:
        res.append((cx, cy))
        ctree_h = int(mat[cy][cx])
        if ctree_h >= vp_h:
            break
        
        cx = cx + dx
        cy = cy + dy
        
    return res


def sol01(data):
    
    x_len = len(data[0])
    y_len = len(data)

    res = set()
    
    #from left
    for y in range(y_len):
        res.update(visible((0, y), (1, 0), data))

    #from right
    for y in range(y_len):
        res.update(visible((x_len-1, y), (-1, 0), data))
    
    #from top
    for x in range(x_len):
        res.update(visible((x, 0), (0, 1), data))
    
    #from bottom
    for x in range(x_len):
        res.update(visible((x, y_len-1), (0, -1), data))
 
    return len(res)


def view_score(x, y, data):
    
    res = 1

    progs = [
            (0, -1),
            (0,  1),
            (-1, 0),
            (1,  0),
        ]
            
    for p in progs:
        res *= len(visible2((x, y), p, data))
    
    return res


def sol02(data):

    res = 0

    for y in range(len(data)):
        for x in range(len(data[0])):
            vs = view_score(x, y, data)
            if vs > res:
                res = vs

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

