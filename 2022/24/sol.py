#!/usr/bin/python


import sys
import copy
import functools
import copy


marks = {
    ">" : ( 1,  0),
    "<" : (-1,  0),
    "^" : ( 0, -1),
    "v" : ( 0,  1),
    }


class Map():


    def __init__(self, mat, marks_pos):
        self.mat = mat
        self.marks_pos = marks_pos
        return


    @functools.cache
    def map_at_turn(self, turn):

        res = [["." for x in range(len(self.mat[0]))] for _ in range(len(self.mat))]
        for y, row in enumerate(self.mat):
            for x, v in enumerate(row):
                if v == "#":
                    res[y][x] = v

        for v, (x, y) in self.marks_pos:
            dx, dy = marks[v]
            dx = dx * turn
            dy = dy * turn

            nx = ((x - 1) + dx) % (len(self.mat[0]) - 2) + 1
            ny = ((y - 1) + dy) % (len(self.mat) - 2) + 1

            if res[ny][nx] == ".":
                res[ny][nx] = v

            elif res[ny][nx] in marks:
                res[ny][nx] = "2"

            elif res[ny][nx].isdigit():
                res[ny][nx] = str(int(res[ny][nx]) + 1)

        return res


    def print_map(self, turn, pos=None):

        res = self.map_at_turn(turn)
        if pos is not None:
            res[pos[1]][pos[0]] = "E"

        for d in res:
            print("".join(d))
        return


def parse_input(text):

    res = [list(x) for x in text.split("\n") if x != ""]

    start = (res[0].index("."), 0)
    end = (res[-1].index("."), len(res) - 1)

    marks_pos = []
    for y, row in enumerate(res):
        for x, v in enumerate(row):
            if v in marks:
                marks_pos.append((v, (x, y)))

    res = Map(res, marks_pos)

    return (res, start, end)


def print_data(data):

    mat, mp, s, e = data

    print(s)
    print(e)
    print(mp)

    print_map(mat, None)
    return


def neighbors(pos, vmap, turn):

    cand = [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)]
    cx, cy = pos

    res = []
    new_map = vmap.map_at_turn(turn+1)
    for dx, dy in cand:
        nx = cx + dx
        ny = cy + dy

        if (
                nx > -1
                and nx < len(new_map[0])
                and ny > -1
                and ny < len(new_map)
                and new_map[ny][nx] == "."
            ):
            res.append((nx, ny))

    return res


def bfs(mat, s, e, sturn=0):

    visited = set()
    queue = [(s, sturn)]
    visited.add((s, sturn))

    while queue:

        v, turn = queue.pop(0)
        if v == e:
            res = turn
            break

        neigh = neighbors(v, mat, turn)
        for w in neigh:
            if (w, turn+1) not in visited:
                visited.add((w, turn+1))
                queue.append((w, turn+1))

    return res


def sol01(data):

    mat, s, e = data
    res = bfs(*data)
    return res


def sol02(data):
    mat, s, e = data
    res = bfs(mat, s, e, sturn=0)
    res = bfs(mat, e, s, sturn=res)
    res = bfs(mat, s, e, sturn=res)
    return res


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)
    #print_data(DATA)

    SOL01 = sol01(DATA)
    print("SOL01: {}".format(SOL01))

    SOL02 = sol02(DATA)
    print("SOL02: {}".format(SOL02))

