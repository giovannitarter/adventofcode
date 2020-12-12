#!/usr/bin/python

import sys
import copy


def print_mat(mat):
    
    print("=====================")
    
    nrs = [" "] + [str(n) for n in list(range(0, len(mat[0])))]
    print(" ".join(nrs))
        
    for idx, i in enumerate(mat):
        print(idx, " ".join(i))
    print("=====================")


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
    #print("neigh ({},{}): {}".format(px, py, res))
    return res


def step(mat, max_occ=4, neig_func=neighbors):

    new_mat = copy.deepcopy(mat)

    for x in range(0, len(mat[0])):
        for y in range(0, len(mat)):

            neigh_c = neig_func(mat, x, y)

            if mat[y][x] == ".":
                replace_mat(new_mat, x, y, ".")

            elif mat[y][x] == "L":
                occ = [mat[ya][xa] for xa, ya in neigh_c if mat[ya][xa] == "#"]
                if len(occ) == 0:
                    replace_mat(new_mat, x, y, "#")

            elif mat[y][x] == "#":
                occ = [mat[ya][xa] for xa, ya in neigh_c if mat[ya][xa] == "#"]
                if len(occ) >= max_occ:
                    replace_mat(new_mat, x, y, "L")

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


def neighbors3(mat, px, py):
    res = []

    mx = len(mat[0])
    my = len(mat)

    def ck_bound(n, mn):
        return(n > -1 and n < mn)

    incs = [
            (0,1), (1,0), (0,-1), (-1,0),
            (1,1), (1,-1), (-1,1), (-1,-1),
            ]

    for inc_x, inc_y in incs:
        off = 1
        
        while True:
            
            x = px + inc_x * off
            if not ck_bound(x, mx):
                break;
            
            y = py + inc_y * off
            if not ck_bound(y, my):
                break;

            if mat[y][x] != ".":
                res.append((x,y))
                break
            
            off = off + 1

    return res


################################
# MAIN
################################

fd = open(sys.argv[1])
text = fd.read()
fd.close()


lines = text.split("\n")
lines = [l for l in lines if l != ""]

last_mat = []
for l in lines:
    last_mat.append(list(l))
mat = copy.deepcopy(last_mat)

print_mat(last_mat)

next_mat = step(last_mat, neig_func=neighbors3, max_occ=5)
print_mat(next_mat)

i = 1
while compare_mat(next_mat, last_mat) == False:
    i = i+1
    print(i)
    last_mat = next_mat
    next_mat = step(last_mat, neig_func=neighbors3, max_occ=5)
    print_mat(next_mat)

count = 0
for i in last_mat:
    count += i.count("#")

print("sol2:")
print(count)

#sys.exit(1)

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

print("sol1:")
print(count)

sys.exit(1)

