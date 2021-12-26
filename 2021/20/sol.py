#!/usr/bin/python


import sys
import copy
#from collections import defaultdict as dd


conv = {
    "." : False,
    "#" : True,
}


class Img():

    def __init__(self, lines, defval):
    
        self.defval = defval
        
        self.min_x = 0
        self.max_x = 0
        self.min_y = 0
        self.max_y = 0

        self.img = {}
        for y, row in enumerate(lines):
            for x, val in enumerate(row):
                if val == "#":
                    self.set(x, y, not defval)

        return

    
    def set(self, x, y, val):

        self.min_x = min([x, self.min_x])
        self.max_x = max([x, self.max_x])
        self.min_y = min([y, self.min_y])
        self.max_y = max([y, self.max_y])

        if val != self.defval:
            self.img[(x, y)] = val
        
        return

    
    def len(self):
        return len(self.img)

    
    def print(self):
        
        for y in range(self.min_y-1, self.max_y+2):
            row = []
            for x in range(self.min_x-1, self.max_x+2):
                val = self.img.get((x, y), self.defval)
                if val == False:
                    val = "."
                else:
                    val = "#"
                row.append(val)
            print("".join(row))
        
        return

    
    def aug_index(self, x, y):
        
        conv_map = [
                (-1, -1),
                ( 0, -1),
                ( 1, -1),
                (-1,  0),
                ( 0,  0),
                ( 1,  0),
                (-1,  1),
                ( 0,  1),
                ( 1,  1),
                ]
        
        aug_idx = []
        for dx, dy in conv_map:
            px = self.img.get((x+dx, y+dy), self.defval)
            aug_idx.append(str(int(px)))
        
        aug_idx = "".join(aug_idx)
        aug_idx = int(aug_idx, 2)
        
        return aug_idx

    
    def step(self, aug):

        if aug[0] == False:
            defval = self.defval
        else:
            defval = not self.defval
    
        tmp = Img([], defval)

        for y in range(self.min_y-1, self.max_y+2):
            row = []
            for x in range(self.min_x-1, self.max_x+2):
                idx = self.aug_index(x, y)
                v = aug[idx]
                tmp.set(x, y, v)

        self.img = tmp.img
        self.min_x = tmp.min_x
        self.max_x = tmp.max_x
        self.min_y = tmp.min_y
        self.max_y = tmp.max_y
        self.defval = defval

        return


def parse_input(text):

    res = None
    lines = [ x for x in text.split("\n\n") if x != "" ]
    
    aug_alg = lines[0]
    aug_alg = [conv[x] for x in aug_alg]

    inp_img = lines[1]
    inp_img = [x for x in lines[1].split("\n")]

    res_img = Img(inp_img, False)

    res = aug_alg, res_img
    return res




if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    AUG, IMG = parse_input(TEXT)

    for i in range(3):
        
        c = IMG.len()
        RES = c
        IMG.step(AUG)
    print("sol01: {}".format(RES))
    
    for i in range(3, 51):
        
        c = IMG.len()
        RES = c
        IMG.step(AUG)
    print("sol02: {}".format(RES))

