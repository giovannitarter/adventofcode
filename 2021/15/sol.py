#!/usr/bin/python


import sys
import copy
import heapq
import itertools


def parse_input(text):

    res = []
    lines = [ x for x in text.split("\n") if x != "" ]
    
    for l in lines:
        row = [ int(x) for x in list(l) ]
        res.append(row)

    return res


def get_neigh(x, y, max_x, max_y):
    
    nmap = [ (-1, 0), (0, -1), (1, 0), (0, 1) ]
    res = []
    
    for nx, ny in nmap:
        
        new_x = x + nx
        new_y = y + ny

        if new_x > -1 and new_y > -1 and new_x < max_x and new_y < max_y:
            res.append((new_x, new_y))

    return res


def dijkstra(mat, source, dest):

    dist = {source: 0}
    prev = {}
    q = [(0, source)]

    while q:

        _, u = heapq.heappop(q)
        
        for v in get_neigh(*u, len(mat[0]), len(mat)):
            alt = dist.get(u, sys.maxsize) + mat[v[1]][v[0]]
            if alt < dist.get(v, sys.maxsize):
                dist[v] = alt
                prev[v] = u
                heapq.heappush(q, (alt, v))
    
    path = []
    
    c = dest
    while c != source:
        path.append(mat[c[1]][c[0]])
        c = prev[c]

    return dist[dest]


def get_mat_larger(x, y, mat):

    ox = x % len(mat[0])
    oy = y % len(mat)
    o_val = mat[oy][ox]

    times_x = x // len(mat[0])
    times_y = y // len(mat)
    new_val = ((o_val + times_x + times_y -1) % 9) + 1
    
    return new_val
    


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)
    
    SRC = (0, 0)
    DST = ((len(DATA[0])-1), len(DATA)-1)

    RES = dijkstra(DATA, SRC, DST)

    print("sol01: {}".format(RES))

    DATA2 = []
    for x in range(len(DATA[0]) * 5):
        row = []
        for y in range(len(DATA) * 5):
            row.append(get_mat_larger(y, x, DATA))
        DATA2.append(row)

    #for d in DATA2:
    #    print(d)
   
    SRC = (0, 0)
    DST = ((len(DATA2[0])-1), len(DATA2)-1)
    #print(DST)
    RES = dijkstra(DATA2, SRC, DST)
    print("sol02: {}".format(RES))

