#!/usr/bin/python


import sys
import copy


N = (0, -1)
S = (0, 1)
E = (1, 0)
W = (-1, 0)

h_sym = {
    N: "^",
    S: "V",
    E: ">",
    W: "<",
}


right = {
    N: [(1, 0), (1, 1)],
    S: [(-1, 0), (-1, -1)],
    E: [(0, 1), (-1, 1)],
    W: [(0, -1), (1, -1)],
    }


s_to_dir = {
    "|": [N, S],
    "-": [W, E],
    "L": [N, E],
    "J": [N, W],
    "7": [S, W],
    "F": [S, E],
}

#opp = {
#    N: S,
#    S: N,
#    E: W,
#    W: E,
#}


#dir_to_s = {}
#for s in s_to_dir:
#    for d in s_to_dir[s]:
#        d = opp[d]
#        tmp = dir_to_s.get(d, [])
#        tmp.append(s)
#        dir_to_s[d] = tmp


dirs = [N, S, W, E]


def find_start(data):
    for y, row in enumerate(data):
        for x, v in enumerate(row):
            if v == "S":
                return(x, y)
    return


def parse_input(text):

    mat = [list(x) for x in text.split("\n") if x != ""]

    res = {}
    for y, row in enumerate(mat):
        for x, v in enumerate(row):
            if v != "S":
                res[(x, y)] = [(x+dx, y+dy) for dx, dy in s_to_dir.get(v, [])]

    start = find_start(mat)

    return mat, start, res


def print_data(data):
    print("\n".join(["".join(d) for d in data]))
    print("")


def walk(first, start, mat, full_mat):

    sx, sy = start
    x_max = len(full_mat[0])
    y_max = len(full_mat)

    visited = [start]
    curr = first
    last = start
    while curr != start:

        cx, cy = curr
        if not (cx > -1 and cx < x_max and cy > -1 and cy < y_max):
            return None, None, None

        next_p = list(mat[curr])

        if last in next_p:
            next_p.remove(last)

        if len(next_p) != 1:
            return None, None, None

        visited.append(curr)
        last = curr
        curr = next_p[0]

    return (len(visited)) // 2, visited, last


def visit(full_mat, start, mat):

    first = None
    last = None

    sx, sy = start
    start_neigh = [(sx+dx, sy+dy) for dx, dy in dirs]
    for first in start_neigh:
        res, visited, last = walk(first, start, mat, full_mat)
        if res:
            break

    first_dir = None
    for k in s_to_dir:
        neigh = [(sx+dx, sy+dy) for dx, dy in s_to_dir[k]]
        if first in neigh and last in neigh:
            first_dir = k
            break

    return res, visited, first_dir


def sol01(data):
    res, visited, p = visit(*data)
    return res


def sol02(data):

    fmat, start, mat = data
    res, visited, p = visit(*data)

    x_max = len(fmat[0])
    y_max = len(fmat)

    sx, sy = start
    mat[start] = p
    fmat[sy][sx] = p


    s_visited = set(visited)
    for y, row in enumerate(fmat):
        for x, v in enumerate(fmat):
            if (x, y) not in s_visited:
                fmat[y][x] = "."

    #print_data(fmat)

    group1 = set()
    for cidx in range(len(visited)):

        lidx = cidx - 1

        last = visited[lidx]
        curr = visited[cidx]
        cx, cy = curr

        diff = curr[0] - last[0], curr[1] - last[1]

        for p in [(curr[0]+dx, curr[1]+dy) for dx, dy in right[diff]]:
            if p not in s_visited:
                tx, ty = p
                if ty < y_max and ty > -1 and tx > -1 and tx < x_max:
                    fmat[ty][tx] = "I"
                    group1.add((tx, ty))

    #print(f"START: {start}, {p}")
    #fmat[start[1]][start[0]] = "S"
    #print_data(fmat)

    queue = set(group1)
    while queue:
        sx, sy = queue.pop()

        for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            nx = sx + dx
            ny = sy + dy
            if nx >= -1 and nx <= x_max and ny >= -1 and ny <= y_max:
                if (nx, ny) not in group1 and (nx, ny) not in s_visited:
                    group1.add((nx, ny))
                    queue.add((nx, ny))


    inside = (-1, -1) in group1

    group1 = [(x, y) for x, y in group1 if x > -1 and x < x_max and y > -1 and y < y_max]
    for x, y in group1:
        if x > -1 and x < x_max and y > -1 and y < y_max:
            fmat[y][x] = "I"


    #print("INTERSECT")
    #print(s_visited.intersection(group1))


    tot = x_max * y_max
    if inside:
        res = tot - len(visited) - len(group1)
    else:
        res = len(group1)

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
