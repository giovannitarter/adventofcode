#!/usr/bin/python


import sys
import copy



def parse_input(text):
    res = [x for x in text.split("\n\n") if x != ""]
    return list(map(lambda x: [list(r) for r in x.split("\n") if r], res))


def print_data(data):
    print("\n".join(["".join(d) for d in data]))


def check_reflection(data, fst, snd):

    i = 1
    while(fst-i >= 0 and snd + i < len(data)):
        if "".join(data[fst-i]) != "".join(data[snd+i]):
            return False
        i = i + 1

    return True


def find_reflection(data, ignore=None):

    res = []
    for idx in range(0, len(data)-1):
        d = data[idx]
        if ignore is not None:
            if idx == ignore -1:
                continue
        if "".join(d) == "".join(data[idx+1]):
            if check_reflection(data, idx, idx+1):
                return idx + 1

    return 0


def sol01(data):

    res = []

    for d in data:
        transposed = list(zip(*d))
        res.append(find_reflection(transposed))
        res.append(find_reflection(d) *100)

    return sum(res)


def all_variations(pattern):

    res = []

    for y, row in enumerate(pattern):
        for x, v in enumerate(row):

            np = copy.deepcopy(pattern)
            if np[y][x] == ".":
                np[y][x] = "#"
            else:
                np[y][x] = "."

            res.append(np)

    return res


def transpose(data):
    return list(zip(*data))


def sol02(data):
    res = []

    for idx, d in enumerate(data):

        found_cols = []
        a = find_reflection(transpose(d))
        if a > 0:
            found_cols.append(a)

        found_rows = []
        b = find_reflection(d)
        if b > 0:
            found_rows.append(b)

        found = False
        new_ds = all_variations(d)
        for nd in new_ds:
            col = find_reflection(transpose(nd), ignore=a)
            row = find_reflection(nd, ignore=b)

            if col != 0 and col not in found_cols:
                res.append(col)
                found_cols.append(col)
                found = True

            if row != 0 and row not in found_rows:
                res.append(row *100)
                found_rows.append(row)
                found = True

        if not found:
            print(f"{idx}: {found}")

    if len(res) != len(data):
        print("ERROR")

    return sum(res)


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)


    SOL01 = sol01(DATA)
    print("SOL01: {}".format(SOL01))

    SOL02 = sol02(DATA)
    print("SOL02: {}".format(SOL02))

    #too low: 27372
    #too low: 34318


