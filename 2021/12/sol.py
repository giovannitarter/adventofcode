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

    return res


def is_big(x):
    return x.upper() == x
    

def all_paths(data, start, end):

    def all_paths_rec(data, curr, end, visited, path):
    
        res = []

        if not is_big(curr):
            visited[curr] = True
        
        path.append(curr)
    
        if curr == end:
            res.append(list(path))
    
        else:
    
            for nv in data[curr]:
                if visited.get(nv, False) == False:
                    res.extend(all_paths_rec(data, nv, end, visited, path))

        path.pop()
        visited[curr] = False
        return res

    
    res = all_paths_rec(data, start, end, {}, [])
    return res


def all_paths2(data, start, end):

    def all_paths_rec(data, curr, end, visited, path):
    
        res = []

        if not is_big(curr):
            visited[curr] = True

        path.append(curr)
    
        if curr == end:
            res.append(list(path))
    
        else:
    
            for nv in data[curr]:
                if visited.get(nv, False) == False:
                    res.extend(all_paths_rec(data, nv, end, visited, path))

        path.pop()
        visited[curr] = False
        return res

    
    res = all_paths_rec(data, start, end, {}, [])
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

    print("")
    RES = all_paths2(DATA, "start", "end")
    RES = len(RES)
    print("sol02 : {}".format(RES))
