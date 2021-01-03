#!/usr/bin/python

import sys
from collections import deque


def parse_text(text):
    res = deque([int(t) for t in text.strip()])
    return res


def move(cups):
    #assuming current cup is cups[0]

    max_cup = max(cups) + 1
    tmp = deque()
    curr = cups.popleft()
    
    for i in range(3):
        tmp.append(cups.popleft())
    
    print("pick up: {}".format(" ".join([str(t) for t in tmp])))

    dst = curr - 1
    while dst not in cups:
        #print(dst)
        dst = (dst - 1) % (max_cup)
    
    print("destination: {}".format(dst))
    
    cups.append(curr)

    #print("rest curr:", cups)

    while cups[0] != dst:
        cups.rotate(-1)
        #print(cups)
    
    cups.rotate(-1)
    #print(cups)
    cups.extend(tmp)
    
    while cups[0] != curr:
        cups.rotate(-1)
    cups.rotate(-1)

    #print(cups)
    #cups.rotate(4)
    #rint(cups.rotate(-1))
    #print(cups)

    return cups


fd = open(sys.argv[1])
text = fd.read()
fd.close()


lines = text.split("\n")
lines = [l for l in lines if l != ""]


cups = parse_text(lines[0])

print(cups)

for i in range(1, 101):
    print("\n-- move {} --".format(i))
    print("cups: {}".format(" ".join([str(c) for c in cups])))
    cups = move(cups)

while cups[0] != 1:
    cups.rotate(1)

tmp = cups.copy()
tmp.popleft()
tmp = list(tmp)
print("".join([str(c) for c in tmp]))



#print(cups[0])

#for l in lines:
#    print(l)



