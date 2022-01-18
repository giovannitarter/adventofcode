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
ROOM_OUT = [(3, 1), (5, 1), (7, 1), (9, 1)]

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



def parse_input(text):

    res = []
    lines = [ x for x in text.split("\n") if x != "" ]

    for l in lines:

        tmp = list(l)
        while len(tmp) < 13:
            tmp.append(" ")
        res.append(tmp)

    return res


def get_neigh(x, y, burrow):

    res = []

    max_x = len(burrow[0])
    max_y = len(burrow)

    cand = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for xm, ym in cand:
        xc = xm + x
        yc = ym + y

        #size check
        if 0 <= xc < max_x and 0 <= yc <= max_y:

            val = burrow[yc][xc]
            if (
                    val not in AMPHIPODS
                    and val != "#"
               ):
                res.append((xc, yc))

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

    q = [(0, start)]
    dist = {start: 0}

    while q:
        _, u = heapq.heappop(q)

        for v in get_neigh(*u, burrow):

            alt = dist.get(u, sys.maxsize) + 1
            if alt < dist.get(v, sys.maxsize):
                dist[v] = alt
                heapq.heappush(q, (alt, v))

    cand = list(dist.keys())
    for c in cand:

        if dist[c] == 0:
            continue

        if c in ROOM_OUT:
            continue

        cx, cy = c
        start_x, start_y = start

        #discard all from hallway to hallway
        if start_y == 1 and cy == 1:
            continue

        #discard if in a room and destination is not hallway
        if start_y > 1 and cy != 1:
            continue

        #always move to the bottom of a room
        if burrow[cy+1][cx] == ".":
            continue

        moving_amp = burrow[start_y][start_x]

        #if moving from hallway to room
        if cy > 1:
            if cx != AMP_ROOMS[moving_amp]:
                continue

        #dont move if already in the right room
        if start_y > 1:
            if start_x == AMP_ROOMS[moving_amp]:
                move = False
                for j in range(start_y, len(burrow)-1):
                    #print(f"j: {moving_amp} {start_x},{j}")
                    if burrow[j][start_x] != moving_amp:
                        move = True
                        break
                if move == False:
                    continue


        res.append((c, dist[c]))


    #print(f"res: {res}")
    return res


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

    res.sort(key=lambda x: x[1])
    #keep = min(len(res), 5)
    #res = res[:keep]

    return res


def is_organized(burrow):

    res = True

    for x, a in [(3, "A"), (5, "B"), (7, "C"), (9, "D")]:

        y = len(burrow)-2
        occ = 0
        while y > 1:
            if burrow[y][x] == a:
                occ += 1
            else:
                break
            y -= 1

        if occ != len(burrow)-3:
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

                #print_burrow(v)

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

    #ORDERED, RES = find_best_path(DATA2)
    #print("ordered:")
    #print_burrow(ORDERED)
    #print("sol02: {}".format(RES))

    etime = perf_counter()
    print(f"time: {etime - stime}")

