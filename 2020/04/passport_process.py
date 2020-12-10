#!/usr/bin/python

import sys


req_fields = [ "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" ]
opt_fields = [ "cid" ]


def validate(passport):

    res = True
    for v in req_fields:
        if v not in passport:
            res = False
            break

    return res



fd = open(sys.argv[1])
text = fd.read()
fd.close()

lines = text.split("\n\n")
lines = [ l.replace("\n", " ") for l in lines if l != "" ]
lines = [ l.strip() for l in lines if l != "" ]


ps = []
valid_ps = []
for l in lines:

    passport = {}
    for r in l.split(" "):
        fields = r.split(":")
        f = fields[0]
        v = fields[1]
        passport[f] = v

    ps.append(passport)


valid_ps = [ p for p in ps if validate(p) ]
print(len(valid_ps))


