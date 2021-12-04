#!/usr/bin/python


import sys


dirs = {
    "up" : (0, 0, 1),
    "down" : (0, 0, -1),
    }


if __name__ == "__main__":

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    LINES = [ x for x in TEXT.split("\n") if x != "" ]
    CMDS = [ tuple(x.split()) for x in LINES ]

    hor = 0
    depth = 0
    aim = 0

    for d, val in CMDS:

        val = int(val)

        if d == "up":
            aim = aim - val

        elif d == "down":
            aim = aim + val

        elif d == "forward":
            hor =  hor + val
            depth = depth + val * aim

        print("")
        print("cmd: {} {}".format(d, val))
        print("cpos: {} {} {}".format(hor, depth, aim))



    print("\nres02 : {}".format(hor * depth))
