#!/usr/bin/python


import sys
import copy



def parse_input(text):

    res = {}
    for y, row in enumerate([list(x.strip()) for x in text.split("\n") if x != ""]):
        for x, v in enumerate(row):
            res[(x, y)] = v

    return res

def serialize(data):
    keys = list(data.keys())
    max_x = max([x for x, y in keys])
    max_y = max([y for x, y in keys])

    res = []
    for y in range(max_y + 1):
        for x in range(max_x +1):
            res.append(data[(x, y)])

    return "".join(res)

def print_data(data):

    keys = list(data.keys())
    max_x = max([x for x, y in keys])
    max_y = max([y for x, y in keys])

    for y in range(max_y + 1):
        line = []
        for x in range(max_x +1):
            line.append(data[(x, y)])
        print("".join(line))

    return


def push_north(data):
    coord = sorted(list(data.keys()), key=lambda x: (x[1], x[0]))
    for x, y in coord:

        if data[(x, y)] != "O":
            continue

        for cy in range(y-1, -1, -1):
            if data[(x, cy)] == ".":
                data[(x, cy)] = "O"
                data[(x, cy+1)] = "."
            else:
                break

    return data


def rotate90cw(data, max_x=None):

    if max_x is None:
        max_x = max([x for x, y in data.keys()])

    return {(max_x - y, x):data[(x, y)] for x, y in data}


def calc_score(data):

    max_y = max([y for x, y in data.keys()])
    res = []
    for x, y in data:
        if data[(x, y)] == "O":
            res.append(max_y + 1 -y)

    return sum(res)

def sol01(data):
    data = copy.deepcopy(data)
    data = push_north(data)
    return calc_score(data)


def sol02(data):

    data = copy.deepcopy(data)

    seen = {}
    series = []
    series_found = False
    i = 0
    while not series_found:

        for _ in range(4):
            data = push_north(data)
            data = rotate90cw(data)

        ser = serialize(data)
        score = calc_score(data)
        k = (ser, score)
        if k in seen:
            series_found = series[seen[k]:]
            break
        else:
            seen[k] = i
            series.append(score)

        i += 1

    res = (1000000000 - len(series)) % len(series_found)
    return(series_found[res-1])


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

    # too low: 96734

