#!/usr/bin/python


import sys
import copy



def parse_input(text):

    res = []
    for line in text.split("\n"):
        if line != "":
            rock = []
            for p in line.split(" -> "):
                x, y = p.split(",")
                rock.append((int(x), int(y)))
            res.append(rock)

    res = create_cave(res)
    return res


def create_cave(data):

    cave = {}

    for line in data:
        line = list(zip(line, line[1:]))
        for ((x1, y1), (x2, y2)) in line:

            if x1 == x2:
                y_max = max(y1, y2)
                y_min = min(y1, y2)
                for y in range(y_min, y_max+1, 1):
                    cave[(x1, y)] = "#"
            elif y1 == y2:
                x_max = max(x1, x2)
                x_min = min(x1, x2)
                for x in range(x_min, x_max+1, 1):
                    cave[(x, y1)] = "#"

    return cave


def cave_to_str(cave):

    xs = [p[0] for p in cave]
    ys = [p[1] for p in cave]

    start_x = min(xs)
    end_x = max(xs)
    start_y = 0
    end_y = max(ys)

    header = []
    for x in range(start_x, end_x+1, 1):
        header.append(list(f"{x: 4}"))
    header = [*zip(*header)]
    header = [" " * 5 + "".join(r) for r in header]

    res = []
    res.extend(header)
    mat = [["." for _ in range(start_x, end_x+1, 1)] for _ in range(end_y+1)]

    for x, y in cave:
        mat[y][x-start_x] = cave[(x,y)]

    res.extend([f"{idx: 4d} " + "".join(r) for idx, r in enumerate(mat)])
    res.extend(header)

    return "\n".join(res)


def neighbors(p, cave):

    res = []
    mask = [(0,1), (-1, 1), (1, 1)]

    for mx, my in mask:
        cx = p[0] + mx
        cy = p[1] + my
        val = cave.get((cx, cy), ".")
        if val not in ["#", "o"]:
            res.append((cx, cy))

    return res


def neighbors2(p, cave, max_y):

    res = []
    mask = [(0,1), (-1, 1), (1, 1)]

    for mx, my in mask:
        cx = p[0] + mx
        cy = p[1] + my

        if cy >= max_y:
            break
        else:
            val = cave.get((cx, cy), ".")

        if val not in ["#", "o"]:
            res.append((cx, cy))

    return res


def add_sand_grain(cave):

    gx = 500
    gy = 0

    max_y = max([p[1] for p in cave])
    #print(f"max_y: {max_y}")

    res = False
    path = [(gx, gy)]
    while gy <= max_y:
        neigh = neighbors((gx, gy), cave)
        if not neigh:
            cave[(gx, gy)] = "o"
            res = True
            break
        else:
            gx = neigh[0][0]
            gy = neigh[0][1]
            path.append((gx, gy))


    return res, path


def add_sand_grain2(cave, max_y):

    gx = 500
    gy = 0


    res = False
    path = [(gx, gy)]
    while True:
        neigh = neighbors2((gx, gy), cave, max_y)
        if not neigh:
            cave[(gx, gy)] = "o"
            res = True
            break
        else:
            gx = neigh[0][0]
            gy = neigh[0][1]
            path.append((gx, gy))

    return res, path


def sol01(data):

    cave = copy.deepcopy(data)
    res = 0
    while True:
        #print(f"\ngrain {res+1}")
        added, path = add_sand_grain(cave)
        if added:
            res += 1
            #print(cave_to_str(cave))

        else:
            break

    #print("\n\n")
    #for p in path:
    #    cave[p] = "~"
    #print(cave_to_str(cave))

    return res


def sol02(data):

    cave = copy.deepcopy(data)
    max_y = max([p[1] for p in cave]) + 2
    res = 0

    while True:
        #print(f"\ngrain {res+1}")
        added, path = add_sand_grain2(cave, max_y)
        res += 1

        if path[-1] == (500, 0):
            break

    #print(cave_to_str(cave))

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

