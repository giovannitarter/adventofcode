#!/usr/bin/python


import sys
import copy



class Dir():

    def __init__(self, name, parent):
        self.name = name
        self.chld = {}
        self.parent = parent


    def __repr__(self):
        return f"- {self.name} (dir)"


    def csize(self):
        res = 0
        for c in self.chld:
            res += self.chld[c].csize()
        return res


class File():

    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent

    def __repr__(self):
        return f"- {self.name} (file, size={self.size})"

    def csize(self):
        return self.size


def parse_input(text):

    res = []
    cmds = [x.strip() for x in text.split("$") if x != ""]

    for c in cmds:
        c = c.split("\n")
        res.append((c[0].split(), c[1:]))

    return res


def build_tree(cmds):

    root = Dir("/", None)
    path = []

    cnode = root
    for cmdline, res in cmds:

        cwd = "/" + "/".join(path)

        #print("")
        #print(f"cwd: {cwd}")
        #print(f"cmd: {cmdline}")

        cmd = cmdline[0]
        args = cmdline[1:]

        if cmd == ("cd"):
            arg = args[0]

            if arg[0] == "/":
                path = [x for x in arg.split("/") if x != ""]

            elif arg == "..":
                path = path[:-1]
                cnode = cnode.parent

            else:
                path.append(arg)
                cnode = cnode.chld[arg]

        elif cmd == "ls":
            chld = {}
            for l in res:
                fields = l.split()
                if fields[0] == "dir":
                    chld[fields[1]] = Dir(fields[1], cnode)
                else:
                    chld[fields[1]] = File(fields[1], int(fields[0]), cnode)
            cnode.chld = chld

    return root


def visit(node, res, path):

    if isinstance(node, Dir):
        res["/" + "/".join(path)] = node.csize()

        for c in node.chld:
            new_path = list(path)
            new_path.append(c)
            visit(node.chld[c], res, new_path)
    return


def sol01(data):

    res = {}
    visit(data, res, [])

    acc = 0
    for r in res:
        if res[r] <= 100000:
            acc += res[r]

    return acc


def sol02(data):

    res = 0

    dirs = {}
    visit(data, dirs, [])
    avail = 70000000
    needed = 30000000

    used = dirs["/"]
    minfree = used - (avail - needed)
    dirs = list(sorted(dirs.items(), key=lambda x: x[1]))
    for d in dirs:
        if d[1] > minfree:
            res = d[1]
            break

    return res


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)
    #print(f"DATA:\n{DATA}\n")

    TREE = build_tree(DATA)
    #print(TREE.csize())

    SOL01 = sol01(TREE)
    print("SOL01: {}".format(SOL01))

    SOL02 = sol02(TREE)
    print("SOL02: {}".format(SOL02))

