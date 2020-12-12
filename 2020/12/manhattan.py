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


#sol1
x = 0
y = 0
ang = 90



for cmd, val in inst:
    
    if cmd == "F":
        cmd = card[ang]

    dx, dy, dang = incs[cmd]
    x = x + val * dx
    y = y + val * dy
    ang = (ang + val * dang) % 360

print(x,y)
print("sol1:", abs(x)  + abs(y))


print("")
#sol2
bx = 0
by = 0

wx = 10
wy = 1

sin = {
    0 : 0,
    90 : 1,
    180 : 0,
    270 : -1,
}

cos = {
    0 : 1,
    90 : 0,
    180 : -1,
    270 : 0,
}


for cmd, val in inst:
    
    if cmd == "F":
        
        mov_x = (wx - bx) * val
        mov_y = (wy - by) * val

        bx = bx + mov_x
        by = by + mov_y
        wx = wx + mov_x
        wy = wy + mov_y

    elif cmd == "R" or cmd == "L":
        rel_x = wx - bx
        rel_y = wy - by

        if cmd == "R":
            val = ((val * -1) % 360)
            #print(val)

        mov_x = rel_x * cos[val] - rel_y * sin[val]
        mov_y = rel_x * sin[val] + rel_y * cos[val]
        #print(mov_x, mov_y)

        wx = bx + mov_x
        wy = by + mov_y
    
    else:
        dx, dy, dang = incs[cmd]
        wx = wx + val * dx
        wy = wy + val * dy


    #print(cmd, val, bx, by, wx-bx, wy-by)

print(bx, by)
print("sol2:", abs(bx)  + abs(by))





