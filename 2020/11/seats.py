#!/usr/bin/python

import sys


fd = open(sys.argv[1])
text = fd.read()
fd.close()


lines = text.split("\n")
lines = [l for l in lines if l != ""]

mat = []
for l in lines:
    mat.append(list(l))


def print_mat(mat):
    print("\n====================")
    for idx, i in enumerate(mat):
        print(idx, "".join(i))
    print("====================")


def replace_mat(mat, x, y, c):

    d = mat[y].pop(x)
    #print("replace ({},{}):{} with {}".format(x, y, d, c))
    mat[y].insert(x, c)
    return


def neighbors(mat, px, py):

    max_x = len(mat[0]) - 1
    max_y = len(mat) - 1

    res = []
    range_y = range(py-1, py+2)
    range_y = [ y for y in range_y if (y >= 0 and y <= max_y)]
    range_x = range(px-1, px+2)
    range_x = [ x for x in range_x if (x >= 0 and x <= max_x)]


    for y in range_y:
        for x in range_x:
            res.append((x,y))

    res.remove((px,py))
    print("neigh ({},{}): {}".format(px, py, res))
    return res


def neighbors2(mat, px, py):

    res = []
    max_x = len(mat[0]) - 1
    max_y = len(mat) - 1

    #west <-
    for x in range(px -1, -1, -1):
        if mat[py][x] != ".":
            res.append((x, py))
            break

    #east ->
    for x in range(px + 1, len(mat[0])):
        if mat[py][x] != ".":
            res.append((x, py))
            break
    #north
    for y in range(py-1, -1, -1):
        if mat[y][px] != ".":
            res.append((px, y))
            break
    #south
    for y in range(py +1, len(mat)):
        if mat[y][px] != ".":
            res.append((px, y))
            break

    #south / east
    max_off = min(len(mat[0])-px, len(mat)-py)
    for off in range(1, max_off):
        x = px+off
        y = py+off
        if mat[y][x] != ".":
            res.append((x, y))
            break

    #south / west
    max_off = min(px, len(mat)-py)+1
    for off in range(1, max_off):
        x = px-off
        y = py+off

        if x>=len(mat[0]) or y >=len(mat):
            break

        if mat[y][x] != ".":
            res.append((x, y))
            break

    #north / east
    max_off = min(py, len(mat)-px) + 1
    #print(max_off)
    for off in range(1, max_off):
        x = px+off
        y = py-off

        if x>=len(mat[0]) or y >=len(mat):
            break

        if mat[y][x] != ".":
            res.append((x, y))
            break

    #north / west
    max_off = min(px, py)+1
    #print(max_off)
    for off in range(1, max_off):
        x = px-off
        y = py-off

        if x>=len(mat[0]) or y >=len(mat):
            break

        if mat[y][x] != ".":
            res.append((x, y))
            break

    return res


def all_mat(mat):
    res = []
    for r in mat:
        res.append(list(r))
    return res


def step(mat, max_occ=4, neig_func=neighbors):

    new_mat = all_mat(mat)
    #print_mat(mat)

    for x in range(0, len(mat[0])):
        for y in range(0, len(mat)):

            #print("aa,", x, y, mat[y][x])

            neigh_c = neig_func(mat, x, y)

            if mat[y][x] == ".":
                replace_mat(new_mat, x, y, ".")

            elif mat[y][x] == "L":
                occ = [mat[ya][xa] for xa, ya in neigh_c if mat[ya][xa] == "#"]
                if len(occ) == 0:
                    replace_mat(new_mat, x, y, "#")
                else:
                    replace_mat(new_mat, x, y, "L")

            elif mat[y][x] == "#":
                occ = [mat[ya][xa] for xa, ya in neigh_c if mat[ya][xa] == "#"]
                if len(occ) >= max_occ:
                    replace_mat(new_mat, x, y, "L")
                else:
                    replace_mat(new_mat, x, y, "#")



            #print([mat[ya][xa] for xa,ya in neigh_c])

            #print_mat(new_mat)

    return new_mat


def compare_mat(mat1, mat2):

    def join(m):
        res = []
        for r in m:
            res.extend(r)
        return res

    tmp1 = join(mat1)
    tmp2 = join(mat2)

    return(tmp1 == tmp2)


#print(test)
#print(neighbors2(mat, *test))


print_mat(mat)
next_mat = step(mat, neig_func=neighbors2, max_occ=5)

i = 1
#while compare_mat(next_mat, mat) == False and i < 50:
while compare_mat(next_mat, mat) == False:
    i = i+1
    mat = next_mat
    next_mat = step(mat, neig_func=neighbors2, max_occ=5)
    print(i)
    print_mat(next_mat)

count = 0
for i in mat:
    count += i.count("#")
#
print(count)

sys.exit(1)

#sol1
print_mat(mat)
next_mat = step(mat)
while compare_mat(next_mat, mat) == False:
    mat = next_mat
    next_mat = step(mat)

print_mat(next_mat)

count = 0
for i in next_mat:
    count += i.count("#")

print(count)

sys.exit(1)

    #print(compare_mat(next_mat, mat))

#replace_mat(mat, 0, 9, "#")
mat = step(mat)
#print(neighbors(mat, 9, 9))
print_mat(mat)

mat2 = step(mat)
print_mat(mat)


print(compare_mat(mat2, mat))


