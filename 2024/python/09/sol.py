#!/usr/bin/python
"""
solution file
"""

import sys
import copy
import time


def timeit(f):

    def timed(*args, **kw):

        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print(f"{f.__name__} took: {te-ts:.4f} sec")
        return result

    return timed


def parse_input(text):
    "input parsing function"
    return [list(map(int, list(x))) for x in text.split("\n") if x != ""][0]


def print_input(data):
    "data print function"
    print(f"DATA:\n{data}\n")


@timeit
def sol01(data):
    "solution for part 1"

    fs = []
    fid = 0
    file = True
    for d in data:
        if file:
            fs.extend(d * [str(fid)])
            fid += 1
        else:
            fs.extend(d * ["."])

        file = not file

    def find_block(lst, frm=None):
        if frm is None:
            i = len(lst) - 1
        else:
            i = frm
        while i > -1:
            if lst[i] != ".":
                break
            i -= 1
        return i

    #print(len(data))
    #print(len(fs))

    lo, hi = 0, find_block(fs)
    old_hi = hi

    while lo < hi:
        if fs[lo] == ".":
            fs[lo] = fs.pop(hi)
            fs.append(".")
            hi = find_block(fs, old_hi)
        lo += 1

    res = 0
    for i, v in enumerate(fs):
        if v != ".":
            res += i * int(fs[i])

    return res


@timeit
def sol02(data):
    "solution for part 2"

    files = []
    pos = 0
    for i, d in enumerate(data):
        if i % 2 == 0:
            files.append((i // 2, pos, d))
        pos += d

    #print(files)

    def find_space(file, files):
        size = file[2]
        start = file[1]

        for fidx, (fid, fstart, fsize) in enumerate(files[:-1]):

            if fstart >= start:
                break

            (nid, nstart, nsize) = files[fidx + 1]
            space_size = nstart - (fstart + fsize)
            if space_size >= size:
                return fidx + 1, fstart + fsize
        return -1, -1

    moved = set()
    cf_idx = len(files) - 1
    while cf_idx > -1:
        cf = files[cf_idx]

        #print(f"\nworking on {cf}")

        if cf[0] in moved:
            cf_idx -= 1
            continue

        s, sdist = find_space(cf, files)
        #print(f"find {cf[0]}", s, sdist)
        if s == -1:
            cf_idx -= 1
            continue
        else:
            moved.add(cf[0])
            mf = files.pop(cf_idx)
            files.insert(s, ((mf[0], sdist, mf[2])))
            #print(files)

    #print(files)

    res = 0
    for f in files:
        res += sum(f[0] * list(range(f[1], f[1] + f[2])))

    return res


if __name__ == "__main__":

    RES = None

    with open(sys.argv[1], encoding="utf8") as fd:
        TEXT = fd.read()

    DATA = parse_input(TEXT)
    #print_input(DATA)
    #SOL01 = sol01(DATA)
    #print(f"SOL01: {SOL01}")
    SOL02 = sol02(DATA)
    print(f"SOL02: {SOL02}")

