#!/usr/bin/python


import sys
import copy
import heapq
from functools import cache
from time import perf_counter


AMPHIPODS = {
        "A" : 1,
        "B" : 10,
        "C" : 100,
        "D" : 1000,
        }

AMP_ROOMS = {
        "A" : 3,
        "B" : 5,
        "C" : 7,
        "D" : 9,
        }

FOLDED = """
  #D#C#B#A#
  #D#B#A#C#
"""

FINAL_STATE = "A#B#C#D"


def parse_input(text):

    res = []
    lines = [ x for x in text.split("\n") if x != "" ]

    for l in lines:

        tmp = list(l)
        while len(tmp) < 13:
            tmp.append(" ")
        res.append(tmp)

    return res


def find_amphipod(burrow):

    res = []
    for y, row in enumerate(burrow):
        for x, val in enumerate(row):
            if val in AMPHIPODS:
                res.append((x, y))

    return res


def print_burrow(burrow):

    for row in burrow:
        txt = "".join(row)
        print(f"{txt}")
    print("")
    return


def all_single_amphipod_moves(burrow, start):

    res = []

    hallway = [(1,1), (2,1), (4,1), (6,1), (8,1), (10,1), (11,1)]

    st_x, st_y = start

    if st_y > 1:

        blocked = False
        for j in range(st_y-1, 0, -1):
            hval = burrow[j][st_x]
            if hval != ".":
                blocked = True
                break

        if not blocked:
            for hp in hallway:

                hx, hy = hp
                hval = burrow[hy][hx]
                if st_x > hx:
                    if hval  == ".":
                        res.append(hp)
                    else:
                        res = []

                elif st_x < hx:
                    if hval == ".":
                        res.append(hp)
                    else:
                        break

    elif st_y == 1:
        amp = burrow[st_y][st_x]
        dst_x = AMP_ROOMS[amp]

        dst_y = None
        for cy in range(len(burrow)-2, 1, -1):
            cval = burrow[cy][dst_x]
            if cval == amp:
                continue

            elif cval == ".":
                dst_y = cy
                break

            else:
                break

        if dst_y is not None:

            cx = st_x
            if cx > dst_x:
                cx -= 1
            elif cx < dst_x:
                cx += 1

            while cx != dst_x:

                if burrow[st_y][cx] != ".":
                    break

                if cx > dst_x:
                    cx -= 1
                elif cx < dst_x:
                    cx += 1

            if cx == dst_x:
                res.append((dst_x, dst_y))

    tmp = []
    for x, y in res:
        dist = abs(x-st_x) + abs(y-st_y)
        tmp.append(((x, y), dist))

    return tmp


def apply_move(amp, dst, cost, burrow):

    res = [list(b) for b in burrow]
    tmp = burrow[amp[1]][amp[0]]
    res[amp[1]][amp[0]] = res[dst[1]][dst[0]]
    res[dst[1]][dst[0]] = tmp

    r_cost = AMPHIPODS[tmp] * cost

    res = (r_cost, res)
    return res


def all_moves(burrow):

    res = []
    amps = find_amphipod(burrow)

    for a in amps:
        moves = all_single_amphipod_moves(burrow, a)
        for dst, cost in moves:
            res.append(apply_move(a, dst, cost, burrow))

    return res


def is_organized(burrow):

    res = True

    tmp = burrow[2:-1]
    for r in tmp:
        cmp = "".join(r[3:10])

        if cmp != FINAL_STATE:
            res = False
            break

    return res


#def h(s_burrow):
#
#    burrow = de_serialize(s_burrow)
#    full = len(burrow)-3
#    res = full * 4
#
#    for x, a in [(3, "A"), (5, "B"), (7, "C"), (9, "D")]:
#
#        y = len(burrow)-2
#        occ = 0
#        while y > 1:
#            if burrow[y][x] == a:
#                occ += 1
#            else:
#                break
#            y -= 1
#
#        res -= occ
#
#    return res


def h(s):
    return 0


def serialize(burrow):
    res = "".join(["".join(b) for b in burrow])
    return res


def de_serialize(burrow):
    res = [list(burrow[i:i+13]) for i in range(0, len(burrow), 13)]
    return res


def find_best_path(burrow):

    res = None

    start = serialize(burrow)
    q = [(0, start)]
    g_score = {start : 0}
    f_score = {start: h(start)}

    prev = {}
    while q:
        _, u = heapq.heappop(q)
        du = de_serialize(u)

        if is_organized(du):
            res = u
            break

        for cost, v in all_moves(du):
            alt = g_score.get(u, sys.maxsize) + cost
            sv = serialize(v)
            if alt < g_score.get(sv, sys.maxsize):

                prev[sv] = u
                g_score[sv] = alt

                hscore = alt + h(sv)
                f_score[sv] = hscore
                heapq.heappush(q, (hscore, sv))

    path = [de_serialize(res)]
    c = prev[res]
    while c != start:
        path.append(de_serialize(c))
        c = prev[c]

    path.reverse()

    if res is not None:
        res = (path, g_score[res])

    return res


def add_folded(burrow):

    res = [list(d) for d in burrow]

    folded = [l for l in FOLDED.split("\n") if l != ""]
    for idx, f in enumerate(folded):
        tmp = list(f)
        while len(tmp) < 13:
            tmp.append(" ")

        res.insert(3+idx, tmp)
    return res



if __name__ == "__main__":

    stime = perf_counter()

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)
    print("initial:")
    print_burrow(DATA)

    ORDERED, RES = find_best_path(DATA)
    print("ordered:")
    print_burrow(ORDERED[-1])
    print("sol01: {}".format(RES))

    print("")
    DATA2 = add_folded(DATA)
    print_burrow(DATA2)

    ORDERED, RES = find_best_path(DATA2)
    print("ordered:")

    #for b in ORDERED:
    #    print_burrow(b)

    print_burrow(ORDERED[-1])
    print("sol02: {}".format(RES))

    etime = perf_counter()
    print(f"time: {etime - stime}")

