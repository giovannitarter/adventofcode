#!/usr/bin/python


import sys
import copy



def parse_input(text):

    res = None
    lines = [ x for x in text.split("\n") if x != "" ]

    template = lines[0]

    expansion = {}
    for l in lines[1:]:
        k, exp = l.split(" -> ")
        expansion[tuple(list(k))] = exp

    return template, expansion


def add_dict(p, times, pmap):
    tmp = pmap.get(p, 0)
    tmp += times
    pmap[p] = tmp
    return pmap


def expand(pair_cnt, lett_cnt, emap):
    

    res = dict()
    for p, p_nr in pair_cnt.items():
        
        new_c = emap[p]
        p1 = (p[0], new_c)
        p2 = (new_c, p[1])

        res = add_dict(p1, p_nr, res)
        res = add_dict(p2, p_nr, res)
        
        lett_cnt = add_dict(new_c, p_nr, lett_cnt)

    return res, lett_cnt


def pair_count(template):
    
    pair_cnt = {}

    for i in range(len(template)-1):
        
        r = tuple(template[i:i + 2])
        
        add_dict(r, 1, pair_cnt)

    return pair_cnt


def count_occurrences(template):

    res = {}
    for c in template:
        add_dict(c, 1, res)

    return res


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    TEMP, EMAP = parse_input(TEXT)

    print("")
    print(f"Template: {TEMP}")

    #for e in EMAP:
    #    print(f"{e} -> {EMAP[e]}")

    PC = pair_count(TEMP) 
    LC = count_occurrences(TEMP)

    for i in range(1, 11):
        PC, LC = expand(PC, LC, EMAP)
        tot = sum(LC.values())
        #print(f"step: {i} -> {tot}")
    
    RES = max(LC.values()) - min(LC.values())
    print("sol01 : {}".format(RES))
    
    for i in range(11, 41):
        PC, LC = expand(PC, LC, EMAP)
        tot = sum(LC.values())
        #print(f"step: {i} -> {tot}")
    
    RES = max(LC.values()) - min(LC.values())
    print("sol02 : {}".format(RES))

