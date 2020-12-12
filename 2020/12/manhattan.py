#!/usr/bin/python

import sys


fd = open(sys.argv[1])
text = fd.read()
fd.close()


lines = text.split("\n")
lines = [l for l in lines if l != ""]


def parse_line(text):
    cmd = text[0]
    val = int(text[1:])
    return((cmd, val))


inst = []
for l in lines:
    inst.append(parse_line(l))



x = 0
y = 0
ang = 90

incs = {
    "N" : (0, 1, 0),
    "S" : (0, -1, 0),
    "E" : (1, 0, 0),
    "W" : (-1, 0, 0),
    "L" : (0, 0, -1),
    "R" : (0, 0, 1)
}

card = {
    0 : "N",
    90 : "E",
    180 : "S",
    270 : "W",
    }


for cmd, val in inst:
    
    if cmd == "F":
        cmd = card[ang]

    dx, dy, dang = incs[cmd]
    x = x + val * dx
    y = y + val * dy
    ang = (ang + val * dang) % 360

print(x,y)
print("sol1:", abs(x)  + abs(y))






