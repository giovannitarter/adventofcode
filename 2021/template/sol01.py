#!/usr/bin/python


import sys
import copy



if __name__ == "__main__":

    RES01 = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    LINES = [ x for x in TEXT.split("\n") if x != "" ]




    print("res01 : {}".format(RES01))
