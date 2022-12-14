#!/usr/bin/python


import sys
import copy
import heapq


def parse_input(text):
    return [list(x) for x in text.split("\n") if x != ""]


def neighbors1(x, y, mat):

    res = []
    val = mat[y][x]

    mask = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for xm, ym in mask:
        cx = x + xm
        cy = y + ym
        if cx > -1 and cy > -1 and cx < len(mat[0]) and cy < len(mat):
            cval = mat[cy][cx]
            if ord(cval) - ord(val) < 2:
                res.append((cx, cy))

    return res


def neighbors2(x, y, mat):

    res = []
    val = mat[y][x]

    mask = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for xm, ym in mask:
        cx = x + xm
        cy = y + ym
        if cx > -1 and cy > -1 and cx < len(mat[0]) and cy < len(mat):
            cval = mat[cy][cx]
            if ord(val) - ord(cval) < 2:
                res.append((cx, cy))

    return res


def Dikstra(mat, source, nfun):

    INF = 1000000

    Q = []
    dist = {
        source: 0,
        }
    prev = {}

    for y, row in enumerate(mat):
        for x, val in enumerate(row):
            if (x, y) != source:
                dist[(x,y)] = INF
            heapq.heappush(Q, (dist[(x, y)], (x, y)))

    while Q:
        _, u = heapq.heappop(Q)

        neigh = nfun(*u, mat)
        for v in neigh:
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(Q, (alt, v))

    return dist, prev


def sol01(data):

    data = copy.deepcopy(data)
    start = None
    end = None
    for y, row in enumerate(data):
        for x, val in enumerate(row):
            if val == "S":
                start = (x, y)
                data[y][x] = "a"
            elif val == "E":
                end = (x, y)
                data[y][x] = "z"

    dist, prev = Dikstra(data, start, neighbors1)
    res = dist[end]
    return res


def sol02(data):

    data = copy.deepcopy(data)
    start = None
    end = []
    for y, row in enumerate(data):
        for x, val in enumerate(row):
            if val == "S" or val == "a":
                end.append((x, y))
                data[y][x] = "a"

            elif val == "a":
                end.append((x, y))

            elif val == "E":
                start = (x, y)
                data[y][x] = "z"

    dist, prev = Dikstra(data, start, neighbors2)

    res = min([dist[e] for e in end])
    return res


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)
    #print(f"DATA:\n{DATA}\n")

    SOL01 = sol01(DATA)
    print("SOL01: {}".format(SOL01))

    SOL02 = sol02(DATA)
    print("SOL02: {}".format(SOL02))

