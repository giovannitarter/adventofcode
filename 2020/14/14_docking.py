#!/usr/bin/python

import sys
import re


def parse_line(l):

    if l.startswith("mask"):
        res = ("mask", l[7:], "")

    elif l.startswith("mem"):
        mt = re.match(r"(mem)\[([0-9]*)\] = ([0-9]*)", l)
        res = mt.groups()

    return res


def apply_mask(val, mask):

    and_mask = int(mask.replace("X", "1"), base=2)
    or_mask = int(mask.replace("X", "0"), base=2)

    val = int(val)
    val = val & and_mask
    val = val | or_mask

    return val


def get_bit(pos):
    and_mask = 1 << pos
    return(pos & and_mask)


def set_bit(pos, val):
    mask = val << pos
    return(pos & mask)


def mask_x(addr, mask):

    addr = "{:036b}".format(int(addr))
    #print(" {}".format(addr))
    res = []
    for i, m in enumerate(mask):
        if m == "1":
            res.append("1")
        elif m == "0":
            res.append(addr[i])
        elif m == "X":
            res.append("X")

    return ("".join(res))


def gen_addrs(mask, addr_p):

    #print("\nmask")

    mask = mask_x(addr_p, mask)

    res = []
    pos = []
    i = 0

    while i < len(mask):
        cp = mask.find("X", i)
        if cp == -1:
            break
        pos.append(cp)
        i = cp + 1

    #print(pos)
    comb_nr = int(1 << len(pos))
    #print(comb_nr)
    #print(mask)
    for c in range(comb_nr):

        fmr = "{:0" + str(len(pos)) + "b}"
        c = fmr.format(c)

        tmp_mask = list(mask)
        for pi, p in enumerate(pos):
            tmp_mask.pop(p)
            tmp_mask.insert(p, c[pi])
        tmp_mask = "".join(tmp_mask)
        #print(tmp_mask)
        res.append(int(tmp_mask, base=2))

    #for c in range(comb_nr):
    #    tmp_nr = int(mask.replace("X", "0"), base=2)
    #    tmp_nr.set_bit()



    #print(res)
    return res


fd = open(sys.argv[1])
text = fd.read()
fd.close()


lines = text.split("\n")
lines = [l for l in lines if l != ""]

cmds = []
for l in lines:
    cmd = parse_line(l)
    cmds.append(cmd)

#SOL1
mask = None
mem = {}

for op, a1, a2 in cmds:

    if op == "mask":
        mask = a1

    elif op == "mem":
        a2 = apply_mask(a2, mask)
        mem[a1] = a2


#print(mem)
sol1 = sum([mem[a] for a in mem])
print(sol1)
print("sol1: {}".format(sol1))

#SOL2
mask = None
addrs = []
mem2 = {}
for op, a1, a2 in cmds:

    if op == "mask":
        mask = a1

    elif op == "mem":
        addrs = gen_addrs(mask, a1)
        for a in addrs:
            mem2[a] = int(a2)


sol2 = sum([mem2[a] for a in mem2])
print(sol2)
print("sol2: {}".format(sol2))
