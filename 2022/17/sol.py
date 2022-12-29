#!/usr/bin/python


import sys
import copy


shapes = (
"""
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
"""
)


def parse_shapes(text):

    res = []
    for shape in text.split("\n\n"):
        shape = [list(l) for l in shape.split("\n") if l != ""]
        tmp = []
        for y, row in enumerate(shape[::-1]):
            for x, v in enumerate(row):
                if v == "#":
                    tmp.append((x, y))

        res.append(tmp)
    return res


def parse_input(text):
    res = [list(x) for x in text.split("\n") if x != ""][0]
    res = Chamber(res, parse_shapes(shapes))
    return res


class Chamber:

    def __init__(self, cmds, shapes):
        self.chmb = {(x, -1):"#" for x in range(7)}
        self.h = -1

        self.tot_shapes = 0

        self.shapes = shapes
        self.s_nr = 0

        self.cmds = cmds
        self.cmd_nr = 0

        self.configs = {}
        self.heights = {0: 0}
        self.cycles_nr = 0

        while True:
            self.add_shape()
            exit, state = self.cycle_check()
            if exit:
                break
        return


    def test_shape(self, x, y, shape):

        res = True
        chmb_px = [(x + cx, y + cy) for cx, cy in shape]

        for xp, yp in chmb_px:

            if xp < 0 or xp > 6:
                res = False
                break

            if self.chmb.get((xp, yp), ".") != ".":
                res = False
                break

        return res, chmb_px


    def add_shape(self):

        self.tot_shapes += 1

        shape = self.shapes[self.s_nr]
        self.s_nr = (self.s_nr + 1) % len(self.shapes)

        sx = 2
        sy = self.h + 4

        while True:
            cmd = self.cmds[self.cmd_nr]
            self.cmd_nr = (self.cmd_nr + 1) % len(self.cmds)

            if cmd == "<":
                nx = sx - 1
            elif cmd == ">":
                nx = sx + 1

            res, _ = self.test_shape(nx, sy, shape)
            if res:
                sx = nx

            ny = sy - 1
            res, _ = self.test_shape(sx, ny, shape)
            if res:
                sy = ny

            else:
                for xp, yp in [(sx + cx, sy + cy) for cx, cy in shape]:
                    self.chmb[(xp, yp)] = "#"
                    if yp > self.h:
                        self.h = yp
                break

        tmp = []
        for x in range(7):
            if self.chmb.get((x, self.h)) == "#":
                tmp.append("#")
        if len(tmp) == 7:
            self.chmb = {(x, self.h):"#" for x in range(7)}

        self.heights[self.tot_shapes] = self.h
        return


    def find_head(self):

        min_y = self.h
        for x in range(7):
            y = self.h
            while y > -1:
                p = self.chmb.get((x, y), ".")
                if p == "#":
                    min_y = min(y, min_y)
                    break
                y = y - 1
        return min_y


    def encode_state(self):

        min_y = self.find_head()-1

        res = []
        max_y = max(self.h, 10)
        for y in range(max_y, min_y, - 1):
            line = [self.chmb.get((x, y), ".") for x in range(7)]
            line = "".join(line)
            res.append(line)
        res = "".join(res)
        return res


    def cycle_check(self):
        state = (self.s_nr, self.cmd_nr, self.encode_state())
        h, cycle_start = self.configs.get(state, (None, None))

        if h is None:
            self.configs[state] = (self.h, self.tot_shapes)
            res = False
        else:

            self.cycle_start = cycle_start
            self.cycle_start_h = h

            self.cycle_len = self.tot_shapes - cycle_start
            self.cycle_h = self.h - h
            res = True

        return res, state


    def compute_shapes_soft(self, nr):

        res = 0
        if nr < self.cycle_start:
            res = self.heights[nr]

        else:

            res = self.cycle_start_h
            nr -= self.cycle_start

            res += ((nr) // self.cycle_len) * self.cycle_h

            idx = ((nr) % self.cycle_len) + self.cycle_start
            res += (self.heights[idx] - self.cycle_start_h)

        res += 1
        return res


    def print_shape_pos(self, sx, sy, shape):

        max_y = max(self.h, 10)
        chmb_px = [(sx + cx, sy + cy) for cx, cy in shape]

        res = []
        for y in range(0, max_y)[::-1]:
            line = []
            for x in range(7):

                if (x, y) in chmb_px:
                    line.append("@")

                else:
                    line.append(self.chmb.get((x, y), "."))

            res.append("".join(line))
        return "\n".join(res)


    def print_top(self):

        min_y = self.find_head() -1

        res = []
        max_y = max(self.h + 2, 10)
        for y in range(max_y, min_y, -1):
            line = [self.chmb.get((x, y), ".") for x in range(7)]
            line = "".join(line)
            res.append(line)
        res.append("")
        print("\n".join(res))
        return


    def __repr__(self):

        max_y = max(self.h + 2, 10)

        res = []
        for y in range(0, max_y)[::-1]:
            line = [self.chmb.get((x, y), ".") for x in range(7)]
            line = "".join(line)
            res.append(line)
        res.append("")
        return "\n".join(res)


def sol01(data):
    return data.compute_shapes_soft(2022)


def sol02(data):
    return data.compute_shapes_soft(1000000000000)


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

