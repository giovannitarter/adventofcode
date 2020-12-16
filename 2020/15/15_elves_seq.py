#!/usr/bin/python

import sys


fd = open(sys.argv[1])
text = fd.read()
fd.close()


lines = text.split("\n")
lines = [l for l in lines if l != ""]


init = [int(x) for x in lines[0].split(",")]
print(init)



test = [0,3,6]

nxt = 0
mem = {}
mem_prev = {}

for i, v in enumerate(test):
    mem_prev[v] = i + 1

seq = list(nxt)
turn = len(test) + 1

while nxt != 2020:
    last = nxt[-1]
    
    new = mem.get(last, 0)
    if new == 0:
        mem[new] = turn
    
    else:
        mem_prev = mem[new]
        mem[new] = last

    seq.append(new)
    turn = turn + 1



