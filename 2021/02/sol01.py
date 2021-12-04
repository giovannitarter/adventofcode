#!/usr/bin/python


import sys


dirs = {
    "forward" : (1, 0),
    "up" : (0, -1),
    "down" : (0, 1),
    }



if __name__ == "__main__":

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    LINES = [ x for x in TEXT.split("\n") if x != "" ]
    CMDS = [ tuple(x.split()) for x in LINES ]

    hor = 0
    depth = 0

    for d, val in CMDS:

        val = int(val)
        transf = dirs[d]

        hor = hor + transf[0] * val
        depth = depth + transf[1] * val

        print("")
        print("cmd: {} {}".format(d, val))
        print("cpos: {} {}".format(hor, depth))



    print("res01 : {}".format(hor * depth))
