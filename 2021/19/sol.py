#!/usr/bin/python


import sys
import copy
import math
import itertools
import heapq
from collections import defaultdict as dd

angles = [ 0, 90, 180, 270 ]

def cos(ang):
    vals = {
        0 : 1,
        90: 0,
        180: -1,
        270: 0,
    }
    return vals[ang]


def sin(ang):
    vals = {
        0 : 0,
        90: 1,
        180: 0,
        270: -1
    }
    return vals[ang]


def rotate(a, b, c):

    return (
        (cos(a)*cos(b), cos(a)*sin(b)*sin(c)-sin(a)*cos(c), cos(a)*sin(b)*cos(c)+sin(a)*sin(c)),
        (sin(a)*cos(b), sin(a)*sin(b)*sin(c)+cos(a)*cos(c), sin(a)*sin(b)*cos(c)-cos(a)*sin(c)),
        (-sin(b),       cos(b)*sin(c)                     , cos(b)*cos(c)                     ),
        )


def all_rotations():

    res = set()
    for x in angles:
        for y in angles:
            for z in angles:
                res.add(rotate(x, y, z))

    return res


def rotate_point(mat, point):

    res = []
    for y, row in enumerate(mat):
        tmp = 0
        for x, val in enumerate(row):
            tmp += val * point[x]
        res.append(tmp)

    return tuple(res)


def vec_sum(a, b):
    return tuple([sum(x) for x in zip(a,b)])


def two_point_distance(a, b):

    xa, ya, za = a
    xb, yb, zb = b
    res = math.sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb) + (za-zb)*(za-zb)) 
    res = (round(res * 1000)) / 1000
    return res


def parse_input(text):

    res = {}
    seqs = [ x for x in text.split("\n\n") if x != "" ]

    for idx, s in enumerate(seqs):
        lines = s.split("\n")
        beacons = [tuple([int(c) for c in x.split(",")]) for x in lines[1:] if x != ""]
        res[idx] = beacons

    return res


def all_beacons_distances(bcns):

    res = {}

    for a, b in itertools.combinations(bcns, 2):
        dist = two_point_distance(a, b)
        res[dist] = tuple(sorted([a, b]))

    return res


def verify_pmap(pmap):
    for a, b in itertools.combinations(pmap.keys(), 2):
        if two_point_distance(a, b) != two_point_distance(pmap[a], pmap[b]):
            return False
    return True

    
def all_mappings_two_lists(A, B):

    res = []

    for pb in itertools.permutations(B):

        new_map = {}
        for idx, a in enumerate(A):
            new_map[a] = pb[idx]
        res.append(new_map)

    return res


def map_points(bcns_a, bcns_b):

    res = {}

    dista = all_beacons_distances(bcns_a)
    distb = all_beacons_distances(bcns_b)
    distc = set(dista.keys()).intersection(set(distb.keys()))

    #print(len(distc))
    
    freq_a = dd(int)
    freq_b = dd(int)
    for d in distc: 
        freq_a[dista[d][0]] += 1
        freq_a[dista[d][1]] += 1
        freq_b[distb[d][0]] += 1
        freq_b[distb[d][1]] += 1

    rem_a = []
    for p, freq in freq_a.items():
        if freq < 11:
            rem_a.append(p)

    #print(rem_a)
    remc = []
    for d in sorted(distc):
        ap1, ap2 = dista[d]
        bp1, bp2 = distb[d]
        if ap1 in rem_a or ap2 in rem_a:
            remc.append(d)

    for rc in remc:
        distc.remove(rc)

    if len(distc) != 66:
        return None

    ap = []
    bp = []
    
    for di in range(2):
        di = distc.pop()
        ap.extend(list(dista[di]))
        bp.extend(list(distb[di]))
    
    for mp in all_mappings_two_lists(ap, bp):
        if verify_pmap(mp):
            pmap = mp
            break

    for d in distc:
        ap1, ap2 = dista[d]
        bp1, bp2 = distb[d]
        
        tmp = dict(pmap)
        tmp[ap1] = bp1
        tmp[ap2] = bp2
        if verify_pmap(tmp):
            pmap = tmp
            continue
        else:
            pmap[ap1] = bp2
            pmap[ap2] = bp1


    #print(len(pmap))
    #for p in sorted(list(pmap.keys())):
    #    print(f"BB: {p} -> {pmap[p]}")

    #if len(pmap) >= 12:
    #    res = pmap
    #else:
    #    res = None

    return pmap


def vec_diff(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def is_aligned(pmap):

    res = True
    tmp = None
    matches = 0

    for pa, pb in pmap.items():

        if tmp is None:
            tmp = vec_diff(pa, pb)
        else:
            if vec_diff(pa, pb) != tmp:
                res = False
                break
            else:
                matches += 1

    return res, tmp


def orient_axis(pmap):

    res = None

    ar = all_rotations()
    for rot in ar:

        new_space = {}
        for p in pmap:
            new_space[p] = rotate_point(rot, pmap[p])

        alg, disp = is_aligned(new_space)

        if alg:
            res = rot, disp
            break

    return res


def dijkstra_paths(mat, start):

    dist = {start: 0}
    prev = {}
    q = [(0, start)]

    while q:
        _, u = heapq.heappop(q)
        for v in mat[u]:
            alt = dist.get(u, sys.maxsize) + 1
            if alt < dist.get(v, sys.maxsize):
                dist[v] = alt
                prev[v] = u
                heapq.heappush(q, (alt, v))

    paths = {}
    for n in mat:

        path = []
        p = n
        while p != start:
            path.append(p)
            p = prev[p]
        path.append(start)
        path.reverse()
        paths[n] = path

    return paths


def conv_point(orig_s, dest_s, point, all_mappings):
    rot, dsp = all_mappings[(orig_s, dest_s)]
    new_pt = vec_sum(rotate_point(rot, point), dsp)
    return new_pt


def to_base(point, orig_s, all_mappings, paths):

    path = list(paths[orig_s])
    path.reverse()

    tmp = point
    for i in range(len(path)-1):
        cs = path[i]
        ns = path[i+1]
        tmp = conv_point(cs, ns, tmp, all_mappings)

    return tmp


def manhattan_dist(a, b):
    
    res = []
    for ac, bc in zip(a, b):
        res.append(abs(ac - bc))
    return sum(res)


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)

    ALL_MAPS = {}
    REGION_ADJ = {}

    for a, b in itertools.combinations(DATA.keys(), 2):

        TMP = map_points(DATA[a], DATA[b])
        if TMP is not None:
            TPL = orient_axis(TMP)
            ALL_MAPS[(b, a)] = TPL

            ADJ = REGION_ADJ.get(a, [])
            ADJ.append(b)
            REGION_ADJ[a] = ADJ

        TMP = map_points(DATA[b], DATA[a])
        if TMP is not None:
            TPL = orient_axis(TMP)
            ALL_MAPS[(a, b)] = TPL

            ADJ = REGION_ADJ.get(b, [])
            ADJ.append(a)
            REGION_ADJ[b] = ADJ


    #print("")
    #for m in sorted(ALL_MAPS):
    #    print(f"{m} -> {ALL_MAPS[m]}")

    #print("")
    #for a in sorted(REGION_ADJ):
    #    print(f"{a} -> {REGION_ADJ[a]}")

    PATHS = dijkstra_paths(REGION_ADJ, 0)
    #print("")
    #for p in sorted(PATHS.keys()):
    #    print(f"{p} -> {PATHS[p]}")

    BCN = set()
    for d in DATA:
        for p in DATA[d]:
            ref_zero = to_base(p, d, ALL_MAPS, PATHS)
            BCN.add(ref_zero)

    RES = len(BCN)
    print("sol01 : {}".format(RES))


    SCANNERS = {}
    for d in DATA:
        ref_zero = to_base((0, 0, 0), d, ALL_MAPS, PATHS)
        SCANNERS[d] = ref_zero

    #for s in SCANNERS:
    #    print(f"{s} -> {SCANNERS[s]}")

    max_manhattan = 0
    for a in SCANNERS:
        for b in SCANNERS:
            tmp = manhattan_dist(SCANNERS[a], SCANNERS[b])
            if tmp > max_manhattan:
                max_manhattan = tmp

    RES = max_manhattan
    print("sol02 : {}".format(RES))
            
