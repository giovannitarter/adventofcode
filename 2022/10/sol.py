#!/usr/bin/python


import sys
import copy


def parse_input(text):
    
    res = []
    for inst in text.split("\n"):
        inst = inst.split()
        if len(inst) == 2:
            if inst[0] == "addx":
                res.append(("unoop", 0))
                res.append(("uaddx", int(inst[1])))
        elif len(inst) == 1:
            if inst[0] == "noop":
                res.append(("unoop", 0))

    return res


def sol01(data):

    cycles = [20]
    cycles.extend(list(range(60, 221, 40)))

    res = 0
    X = 1
    for c_nr, inst in enumerate(data):

        if c_nr + 1 in cycles:
            res = res + X * (c_nr + 1)
        
        inst, val = inst
        if inst == "unoop":
            pass
        elif inst == "uaddx":
            X = X + val
    
    return res


def screen_str(screen):

    return "\n" + "\n".join(["".join(row) for row in screen]) + "\n"


def sol02(data):

    screen_x = 40
    screen_y = 6
    screen = [["." for _ in range(screen_x)] for _ in range(screen_y)]
    
    X = 1
    for c_nr, inst in enumerate(data):
        
        sprite_pos = [X-1, X, X+1]
        cpx_x = c_nr % 40
        cpx_y = c_nr // 40

        if cpx_x in sprite_pos:
            screen[cpx_y][cpx_x] = "#"

        inst, val = inst
        if inst == "unoop":
            pass
        elif inst == "uaddx":
            X = X + val
    
    res = screen_str(screen)
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

