#!/usr/bin/python

import sys




fd = open(sys.argv[1], "r")
text = fd.read()
fd.close()

lines = text.split("\n")
lines = [ l for l in lines if l != "" ]
entries = [ int(i.strip()) for i in lines ]

for x1 in entries:
    for x2 in entries:
        for x3 in entries:
            if (x1 + x2 + x3) == 2020:
                print(x1)
                print(x2)
                print(x3)
                print(x1 * x2 * x3)







