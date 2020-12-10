#!/usr/bin/python


import sys
import re


fd = open(sys.argv[1])
text = fd.read()
fd.close()

lines = text.split("\n")
lines = [ l for l in lines if l != "" ]
lines = [ l.strip() for l in lines ]


db = []
res = 0
for l in lines:
    m = re.match("(?P<min>\d*)-(?P<max>\d*) (?P<char>\D): (?P<pass>\D*)", l)
    db.append(m.groupdict())


for d in db:

    mn = int(d["min"])
    mx = int(d["max"])
    occ = d["pass"].count(d["char"])

    if occ >= mn and occ <= mx:
        res = res + 1

print("res1")
print(res)


res = 0
for d in db:

    tmp = 0
    p1 = int(d["min"]) - 1
    p2 = int(d["max"]) - 1
    ps = d["pass"]

    #print("\n")
    #print(p1)
    #print(p2)
    #print(ps)
    #print(d["char"])

    if p1 < len(ps) and ps[p1] == d["char"]:
        tmp = tmp + 1

    if p2 < len(ps) and ps[p2] == d["char"]:
        tmp = tmp + 1

    if tmp == 1:
        res = res + 1

print("res2")
print(res)



