#!/usr/bin/python

import sys


def parse_line(l):
    
    fields = l.split(" ")
    op = fields[0]
    val = int(fields[1])
    
    return(op, val)


def run_code(inst):

    res = False
    ip = 0
    acc = 0
    visited = {}
    
    while ip < len(inst):
    
        #print("\n================")
        #print("will run {}. {}".format(ip, inst[ip]))
    
        if visited.get(ip) is None:
            visited[ip] = True
        else:
            print("second time, break")
            print(acc)
            break
    
        ci, arg = inst[ip]
    
        if ci == "nop":
            ip = ip + 1
        
        elif ci == "acc":
            acc = acc + arg
            ip = ip + 1
    
        elif ci == "jmp":
            ip = ip + arg

    if ip >= len(inst):
        print("successfully terminated!")
        print(acc)
        res = True

    return res


fd = open(sys.argv[1])
text = fd.read()
fd.close()


lines = text.split("\n")
lines = [l for l in lines if l != ""]

inst = []
for l in lines:
    inst.append(parse_line(l))


for addr, ci in enumerate(inst):
    print("{}. -> {} {}".format(addr, *ci))



for idx, i in enumerate(inst):

    print(i)
    
    if i[0] == "nop":
        new_i = ("jmp", i[1])
    
    elif i[0] == "jmp":
        new_i = ("nop", i[1])
    
    else:
        continue
    
    print("changing inst {}".format(idx))

    tmp_lst = list(inst)
    tmp_lst.pop(idx)
    tmp_lst.insert(idx, new_i)

    if run_code(tmp_lst):
        print(idx)
        break


