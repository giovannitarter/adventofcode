#!/usr/bin/python

import sys
import copy


START_X = 0
START_Y = 4

moves = {
    "R" : ( 1, 0),
    "L" : (-1, 0),
    "U" : (0, -1),
    "D" : (0,  1),
    }


def parse_input(text):
    res = [x.split() for x in text.split("\n") if x != ""]
    return res


def print_mat(rope):

    x_max = max([rope[k][0] for k in rope])
    x_min = min([rope[k][0] for k in rope])
    x_nr = max(6, x_max-x_min+1)
    disp_x = 0 - x_min
    
    y_max = max([rope[k][1] for k in rope])
    y_min = min([rope[k][1] for k in rope])
    y_nr = max(5, y_max-y_min+1)
    disp_y = 0 - y_min

    mat = [["." for _ in range(x_nr)] for _ in range(y_nr)]
    
    for k in sorted(list(rope.keys()), reverse=True):
        kx, ky = rope[k]

        if k == 0:
            tmp = "H"
        elif k == 1 and len(rope.keys()) == 2:
            tmp = "T"
        else:
            tmp = str(k)
        
        mat[ky+disp_y][kx+disp_x] = tmp
    
    for row in mat:
        print("".join(row))
    print("")
    
    return


def update_tail(tpos, hpos):

    tx, ty = tpos
    hx, hy = hpos

    hor = hx - tx
    ver = hy - ty

    if abs(hor) <= 1 and abs(ver) <= 1:
        pass
    
    elif hor == 0 and ver != 0:
        ty = ty + ver // abs(ver)
    
    elif hor != 0 and ver == 0:
        tx = tx + hor // abs(hor)

    else:
        ty = ty + ver // abs(ver)
        tx = tx + hor // abs(hor)

    tpos = (tx, ty)
    return tpos


def sol(data, rope_sec=10):
    
    res = set()
    
    rope = {}
    for i in range(rope_sec):
        rope[i] = (START_X, START_Y)

    res.add(rope[rope_sec-1])
    #print_mat(rope)

    for dir, step in data:

        #print(f"== {dir} {step} ==\n")

        dx = moves[dir][0]
        dy = moves[dir][1]
        step = int(step)
        for _ in range(step):
            rope[0] = (rope[0][0] + dx, rope[0][1] + dy)
            for k in range(1, rope_sec):
                new_pos = update_tail(rope[k], rope[k-1])
                rope[k] = new_pos

            res.add(rope[rope_sec-1])

    #print_mat(rope)
    res = len(res)
    return res


def sol01(data):
    return sol(data, rope_sec=2)


def sol02(data):
    return sol(data)


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

