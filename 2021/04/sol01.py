#!/usr/bin/python


import sys
import copy


def transpose(mat):
    return [list(x) for x in zip(*mat)]


class Board():

    def __init__(self, mat):
        
        self.mat = []
        for r in mat:
            self.mat.append([(n, False) for n in r])

        return


    def mark(self, nr):

        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                if self.mat[i][j][0] == nr:
                    self.mat[i][j] = (nr, True)

        return


    def print(self):
        
        print("")
        for r in self.mat:
            print(r)
        return


    def check(self):
        
        res = None
        for row in self.mat:
            if len([x for x in row if x[1] == True]) == 5:
                res = True
                break

        if not res:
            for col in transpose(self.mat):
                if len([x for x in col if x[1] == True]) == 5:
                    res = True
                    break

        if res:
            res = []
            for c in self.mat:
                res.extend([int(x[0]) for x in c if x[1] == False])
            res = sum(res)

        return res




if __name__ == "__main__":

    RES01 = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    LINES = [ x for x in TEXT.split("\n") if x != "" ]


    drawn = LINES.pop(0).split(",")
    print(drawn)

    boards = []
    for i in range(0, len(LINES), 5):
        boards.append(Board([ b.split() for b in LINES[i:i+5] ]))

    for d in drawn:
        print("Drawn {}".format(d))

        w_unmarked = None
        for b in boards:
            b.mark(d)
            b.print()
            res = b.check()
            if res is not None:
                w_unmarked = res
                print(res)
                break
        
        if w_unmarked is not None:
            RES01 = int(d) * w_unmarked 
            break
        print("")


    print("res01 : {}".format(RES01))
