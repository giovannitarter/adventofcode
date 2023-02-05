#!/usr/bin/python


import sys
import copy
import re

#clockwise
#initially right
DIR_MASK = [(1, 0), (0, 1), (-1, 0), (0, -1)]
D_RIGHT = 0
D_DOWN = 1
D_LEFT = 2
D_UP = 3

MARKS = {

        0 : ">",
        1 : "V",
        2 : "<",
        3 : "^",
        }

MARKS_TO_OR = {v:k for (k,v) in MARKS.items()}

def compute_ext(mat):

    res = []

    for row in mat:

        for x, v in enumerate(row):
            if v != " ":
                start = x
                break

        for x, v in enumerate(row[::-1]):
            if v != " ":
                end = len(row) - x
                break

        res.append((start, end, end - start))
    return res


def parse_input(text):

    res = None
    mat, dirs = text.split("\n\n")

    dirs = dirs.strip()
    dirs = re.findall(r"\d+|[RL]", dirs)

    rows = []
    ext = []

    max_len = 0
    for row in mat.split("\n"):
        row = list(row)
        rows.append(row)
        max_len = max(max_len, len(row))

    for row in rows:
        if len(row) < max_len:
            row.extend([" "] * (max_len - len(row)))

    hor_ext = compute_ext(rows)
    ver_ext = compute_ext(list(zip(*rows)))

    res = ((rows, hor_ext, ver_ext), dirs)
    return res


def print_data(data):

    (rows, hor_ext, ver_ext), dirs = data
    for y, row in enumerate(rows):
        ranges = str(hor_ext[y])
        row = "".join(row)
        #print(f"{ranges:15} -  {row}")
        print(f"{row}")

    #for x, rng in enumerate(ver_ext):
    #    print(f"x: {x} - {rng}")

    return


def print_data_pos(data, pos):

    cx, cy, cor = pos
    (rows, hor_ext, ver_ext), dirs =  copy.deepcopy(data)


    mark = MARKS[cor]
    rows[cy][cx] = mark
    for y, row in enumerate(rows):
        ranges = str(hor_ext[y])
        row = "".join(row)
        #print(f"{y:5} - {row}")
        print(f"{row}")

    return


def next_tile01(cx, cy, cor, mask, hor_ext, ver_ext):

    if mask[0] != 0:
        sx, ex, lx = hor_ext[cy]
        nx = (((cx - sx) + mask[0]) % lx) + sx
        ny = cy

    elif mask[1] != 0:
        sy, ey, ly = ver_ext[cx]
        ny = (((cy - sy) + mask[1]) % ly) + sy
        nx = cx

    return nx, ny, cor, mask


def get_tile_edges(x, y, l):

	edges = {
		0 : [(x*l, i) for i in range(y*l, (y+1)*l)],
		1 : [(i, (y+1)*l) for i in range(x*l, (x+1)*l)],
		2 : [((x+1)*l, i) for i in range(y*l, (y+1)*l)],
		3 : [(i, y*l) for i in range(x*l, (x+1)*l)],
	}
	return edges


def next_tile02(cx, cy, cor, mask, hor_ext, ver_ext):

    """
	0   1   2   3
  0         1111
	        1111
	        1111
	        1111
  1 222233334444
	222233334444
	222233334444
	222233334444
  2	        55556666
	        55556666
	        55556666
	        55556666


	face 1 -> 6 4 3 2
	face 2 -> 3 5 6 1
	face 3 -> 4 5 2 1
	face 4 -> 6 5 3 1
	face 5 -> 6 2 3 4
	face 6 -> 1 2 5 4
    """

    nx = cx
    ny = cy
    nor = cor
    nmask = mask

    #Face 1
    #edge 0
    if (
            cx == 3 * el -1 and
            cy >= 0 * el and
            cy <  1 * el and
            cor == 0
        ):
        ny = ((el-1) - (cy % el)) + 2 * el
        nx = cx + el
        nor = 2
        nmask = (-1, 0)


    #Face 1
    #edge 2
    #(2, 0) -> (1, 1)
    elif (
            cx == 2 * el and
            cy >= 0 * el and
            cy <  1 * el and
            cor == 2
        ):
        nx = (cy % el) + 1 * el
        ny = el * 1
        nor = 1
        nmask = (0, 1)

    #Face 1 -> Face 2
    #edge 3
    #(2, 0) -> (0, 1)
    elif (
            cy == 0 * el and
            cx >= 2 * el and
            cx <  3 * el and
            cor == 3
        ):
        ny = el * 1
        nx = (el-1 - (cx % el)) + 0 * el
        nor = 1
        nmask = (0, 1)


    #Face 2 -> Face 1
    #edge 3
    #(2, 0) -> (0, 1)
    elif (
            cy == 1 * el and
            cx >= 0 * el and
            cx <  1 * el and
            cor == 3
        ):
        ny = el * 0
        nx = (el-1 - (cx % el)) + 2 * el
        nor = 1
        nmask = (0, 1)


    #Face 2 -> Face 5
    #edge 1
    #(0, 1) -> (2, 2)
    elif (
            cx >= (0 + 0) * el and
            cx <  (0 + 1) * el and
            cy >= (1 + 0) * el + el - 1  and
            cy <  (1 + 1) * el and
            cor == D_DOWN
        ):
        nx = (el - 1 - (cx % el)) + (0 + 2) * el
        ny = ((2 + 1) * el)-1
        nor = D_UP
        nmask = (0, -1)


    #Face 2 -> Face 6
    #edge 2
    #(0, 1) -> (3, 2)
    elif (
            #src   x
            cx >= (0 + 0) * el and
            #src   x
            cx <  (0 + 1) * el - (el-1) and
            #src   y
            cy >= (1 + 0) * el and
            #src   y
            cy <  (1 + 1) * el and
            cor == D_LEFT
        ):

        #dest                        x
        nx = (el - 1 - (cy % el)) + (3 + 0) * el

        #dest  y
        ny = ((2 + 1) * el) - 1

        nor = D_UP
        nmask = (0, -1)

    #Face 3 -> Face 5
    #edge 1
    #(1, 1) -> (2, 2)
    elif (
            #src   x
            cx >= (1 + 0) * el and
            #src   x
            cx <  (1 + 1) * el and
            #src   y
            cy >= (1 + 1) * el -1 and
            #src   y
            cy <  (1 + 1) * el and
            cor == D_DOWN
        ):

        #dest                        x
        nx = (2 + 0) * el

        #dest  y
        ny = (el - 1 - (cx % el)) + (2 + 0) * el

        nor = D_RIGHT
        nmask = DIR_MASK[nor]

    #Face 3
    #edge 3
    #(0, 1) -> (2, 0)
    elif (
            cy == 1 * el and
            cx >= 1 * el and
            cx <  2 * el and
            cor == 3
        ):
        nx = el * 2
        ny = (cx % el) + 0 * el
        nor = 0
        nmask = (1, 0)


    #Face 4 -> Face 6
    #edge 0
    #(2, 1) -> (3, 2)
    elif (
            #src   x
            cx >= (2 + 1) * el -1 and
            #src   x
            cx <  (2 + 1) * el and
            #src   y
            cy >= (1 + 0) * el and
            #src   y
            cy <  (1 + 1) * el and
            cor == D_RIGHT
        ):

        #dest                        x
        nx = el - 1 - (cy % el) + (3 + 0) * el

        #dest  y
        ny = (2 + 0) * el

        nor = D_DOWN
        nmask = DIR_MASK[nor]


    #Face 5 -> Face 2
    #edge 2
    #(2, 2) -> (0, 1)
    elif (
            #src   x
            cx >= (2 + 0) * el and
            #src   x
            cx <  (2 + 1) * el and
            #src   y
            cy >= (2 + 0) * el + el - 1  and
            #src   y
            cy <  (2 + 1) * el and
            cor == D_DOWN
        ):

        #dest                        x
        nx = (el - 1 - (cx % el)) + (0 + 0) * el
        #dest  y
        ny = ((1 + 1) * el) - 1

        nor = D_UP
        nmask = (0, -1)


    #Face 5 -> Face 3
    #edge 2
    #(2, 2) -> (1, 1)
    elif (
            #src   x
            cx >= (2 + 0) * el and
            #src   x
            cx <  (2 + 0) * el + 1 and
            #src   y
            cy >= (2 + 0) * el and
            #src   y
            cy <  (2 + 1) * el and
            cor == D_LEFT
        ):

        #dest                        x
        nx = (el - 1 - (cy % el)) + (1 + 0) * el

        #dest  y
        ny = (1 + 1) * el -1

        nor = D_UP
        nmask = DIR_MASK[nor]

    #Face 6
    #edge 0
    elif (
            cx == 4 * el -1 and
            cy >= 2 * el and
            cy <  3 * el and
            cor == 0
        ):
        ny = ((el-1) - (cy % el)) + 0 * el
        nx = 3 * el - 1
        nor = 2
        nmask = (-1, 0)

    #Face 6 -> Face 2
    #edge 1
    #(3, 2) -> (0, 1)
    elif (
            #src   x
            cx >= (3 + 0) * el and
            #src   x
            cx <  (3 + 1) * el and
            #src   y
            cy >= ((2 + 1) * el) -1 and
            #src   y
            cy <  (2 + 1) * el and
            cor == D_DOWN
        ):

        #dest  x
        nx = ((0 + 0) * el)

        #dest  y
        ny = (el - 1 - (cx % el)) + (1 + 0) * el

        nor = D_RIGHT
        nmask = (1, 0)


    #Face 6 -> Face 4
    #edge 3
    #(3, 2) -> (2, 1)
    elif (
            #src   x
            cx >= (3 + 0) * el and
            #src   x
            cx <  (3 + 1) * el and
            #src   y
            cy >= (2 + 0) * el and
            #src   y
            cy <  (2 + 0) * el + 1 and
            cor == D_UP
        ):

        #dest                        x
        nx = (2 + 1) * el - 1

        #dest  y
        ny = (el - 1 - (cx % el)) + (1 + 0) * el

        nor = D_LEFT
        nmask = DIR_MASK[nor]

    elif mask[0] != 0:
        #sx, ex, lx = hor_ext[cy]
        nx = cx + mask[0]
        ny = cy

    elif mask[1] != 0:
        #sy, ey, ly = ver_ext[cx]
        ny = cy + mask[1]
        nx = cx

    #print(nx, ny, nor, nmask)
    return nx, ny, nor, nmask


def cube_progression(cx, cy, cor, d, data):

    (mat, hor_ext, ver_ext), _ = data

    dprint = print

    dprint("\n\n\n==================================================================")
    dprint(f"Initial")
    dprint(f"{cx} {cy} {cor} {d}")
    print_data_pos(data, (cx, cy, cor))

    cmask = DIR_MASK[cor]
    for step in range(d):

        dprint("\n==================================================================")
        dprint(f"step: {step+1}/{d}")
        cx, cy, cor, cmask = next_tile02(cx, cy, cor, cmask, hor_ext, ver_ext)
        print_data_pos(data, (cx, cy, cor))

    dprint("\n==================================================================")
    dprint(f"Final")
    print_data_pos(data, (cx, cy, cor))
    return cx, cy, cor


def sol(data, next_tile_func):

    (mat, hor_ext, ver_ext), dirs = data

    cy = 0
    cx = mat[0].index(".")
    cor = 0

    print(f"start: {cx} {cy} {cor}")

    for idx, d in enumerate(dirs):

        if d == "L":
            cor = (cor - 1) % len(DIR_MASK)

        elif d == "R":
            cor = (cor + 1) % len(DIR_MASK)

        else:

            dist = int(d)
            cmask = DIR_MASK[cor]
            for _ in range(dist):

                nx, ny, nor, nmask = next_tile_func(cx, cy, cor, cmask, hor_ext, ver_ext)

                if mat[ny][nx] == ".":
                    cx = nx
                    cy = ny
                    cor = nor
                    cmask = nmask

                elif mat[ny][nx] == "#":
                    break

                else:
                    print(f"cannot proceed to {nx} {ny}")
                    sys.exit(1)

                #print_data_pos(data, (cx, cy, cor))

    return (cx, cy, cor)


def encode_sol(sol):
    cx, cy, cor = sol
    return (cy + 1) * 1000 + (cx + 1) * 4 + cor


def rotate_90_cw(mat):
    res = list(zip(*mat[::-1]))

    #for y, row in enumerate(res):
    #    for x, v in enumerate(row):
    #        if v in MARKS_TO_OR:
    #            row[x] = MARKS[(MARKS_TO_OR[v] + 1) % len(MARKS_TO_OR)]

    return res



def transform(data, org, dst, rot):

    (mat, hor_ext, ver_ext), dirs = data

    xb, yb = org

    xmin = xb * el
    xmax = (xb+1) * el
    ymin = yb * el
    ymax = (yb+1) * el

    sub_mat = [mat[y][xmin:xmax] for y in range(ymin, ymax)]

    for i in range(rot):
        sub_mat = rotate_90_cw(sub_mat)

    #for row in sub_mat:
    #    print("".join(row))

    x_dst_max = (dst[0] + 1) * el
    for row in mat:
        if len(row) < x_dst_max:
            row.extend([" "] * (x_dst_max - len(row)))
            ver_ext = [""] * x_dst_max

    y_dst_max = (dst[1] + 1) * el
    if len(mat) < y_dst_max:
        mat.extend([[" "] * x_dst_max for _ in range(y_dst_max-len(mat))])
        hor_ext = [""] * y_dst_max


    for y, row in enumerate(sub_mat):
        for x, _ in enumerate(row):

            x_org = x + (org[0] * el)
            y_org = y + (org[1] * el)

            x_dst = x + (dst[0] * el)
            y_dst = y + (dst[1] * el)

            mat[y_dst][x_dst] = sub_mat[y][x]
            mat[y_org][x_org] = " "


    return ((mat, hor_ext, ver_ext), dirs)


def ref_to_input_cn(data):

    res = data
    res = transform(res, (2, 0), (1, 0), 0)
    res = transform(res, (0, 1), (0, 3), 3)
    res = transform(res, (1, 1), (0, 2), 3)
    res = transform(res, (2, 1), (1, 1), 0)
    res = transform(res, (2, 2), (1, 2), 0)
    res = transform(res, (3, 2), (2, 0), 2)
    return res


def input_to_ref_cn(data):

    res = data
    res = transform(res, (2, 0), (3, 2), 2)
    res = transform(res, (1, 2), (2, 2), 0)
    res = transform(res, (1, 1), (2, 1), 0)
    res = transform(res, (0, 2), (1, 1), 1)
    res = transform(res, (0, 3), (0, 1), 1)
    res = transform(res, (1, 0), (2, 0), 0)
    return res


def sol01(data):
    res = sol(data, next_tile01)
    return encode_sol(res)


def sol02(data):

    if sys.argv[1] == "input":
        tmp = input_to_ref_cn(data)
    else:
        tmp = data

    res = sol(tmp, next_tile02)
    print(res)

    mat = tmp[0][0]
    mat[res[1]][res[0]] = MARKS[res[2]]

    tmp = ((mat, tmp[0][1], tmp[0][2]), tmp[1])
    tmp = ref_to_input_cn(tmp)

    for y, row in enumerate(tmp[0][0]):
        for x, v in enumerate(row):
            if v not in [".", "#", " "]:
                return(encode_sol((x, y, (MARKS_TO_OR[v] + 3) % 4)))


    #res = encode_sol((x, y, (res[2] + 3) % 4))
    #res = encode_sol((8, 161, 2))
    return res


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)
    print_data(DATA)

    if sys.argv[1] == "test":
        el = 4
    elif sys.argv[1] == "input":
        el = 50
    else:
        print("input is not test or input")

    SOL01 = sol01(DATA)
    print("SOL01: {}".format(SOL01))

    #DATA = ref_to_input_cn(DATA)
    #DATA = input_to_ref_cn(DATA)


    # 59159 -> too low
    # 200802 -> too high
    SOL02 = sol02(DATA)
    print("SOL02: {}".format(SOL02))

