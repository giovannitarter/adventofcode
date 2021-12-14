#!/usr/bin/python


import sys
import copy



def parse_input(text):

    res = dict()
    lines = [ x for x in text.split("\n") if x != "" ]

    for l in lines:
        n1, n2 = l.split("-")

        tmp = res.get(n1, [])
        tmp.append(n2)
        res[n1] = tmp

        tmp = res.get(n2, [])
        tmp.append(n1)
        res[n2] = tmp

    for r in res:
        if "start" in res[r]:
            res[r].remove("start")
        res[r].sort()

    res["end"] = []

    return res


def is_big(x):
    return x.upper() == x


def all_paths(data, start, end):

    def all_paths_rec(data, curr, end, path):

        res = []

        path.append(curr)

        if curr == end:
            res.append(list(path))

        else:

            nexts = []
            for c in data[curr]:

                if c == "start":
                    continue

                if is_big(c):
                    nexts.append(c)

                else:
                    if c not in path:
                        nexts.append(c)

            for nv in nexts:
                res.extend(all_paths_rec(data, nv, end, path))

        path.pop()
        return res


    res = all_paths_rec(data, start, end, [])
    return res


def all_paths2(data, start, end):

    def all_paths_rec(data, curr, end, path, twice):

        res = []

        path.append(curr)

        if curr == end:
            res.append(list(path))

        else:

            for nv in data[curr]:

                if is_big(nv):
                    res.extend(all_paths_rec(data, nv, end, path, twice))

                else:
                    if nv not in path:
                        res.extend(all_paths_rec(data, nv, end, path, twice))
                    else:
                        if twice is False:
                            res.extend(all_paths_rec(data, nv, end, path, True))

        path.pop()
        return res


    res = all_paths_rec(data, start, end, [], False)

    #for r in res:
    #    print(r)

    return res


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)
    for d in DATA:
        print(f"{d} -> {DATA[d]}")

    print("")
    RES = all_paths(DATA, "start", "end")
    RES = len(RES)
    print("sol01 : {}".format(RES))

    RES = all_paths2(DATA, "start", "end")
    RES = len(RES)
    print("sol02 : {}".format(RES))
