#!/usr/bin/python


import sys
import copy
import os


LV = 4

class Message():

    def __init__(self, message, start=0):
    
        mss = message[start:]
        self.ver = int(mss[0:3], 2)
        self.mid = int(mss[3:6], 2)
        self.subpackets = []

        if self.mid == LV:
            
            cnt = True
            pos = 6
            lval = []
            while cnt:
                val = mss[pos:pos+5]
                
                if val[0] == "0":
                    cnt = False
                
                pos = pos + 5
                lval.append(val[1:])
                 
            
            lval = "".join(lval)
            self.lval = int(lval, 2)
            #print(f"lval: {self.lval}")
            self.next = pos


        else:
            ltid = mss[6]
            if ltid == "0":

                remaining = int(mss[7:7+15], 2)
                parsed = 0
                while parsed < remaining: 
                    msg = Message(mss, start=7+15+parsed)
                    self.subpackets.append(msg)
                    parsed += msg.next
                self.next = 7 + 15 + parsed
            
            else:
                subpackets_nr = int(mss[7:7+11], 2)
                
                parsed = 0
                for i in range(subpackets_nr):
                    msg = Message(mss, start=7+11+parsed)
                    self.subpackets.append(msg)
                    parsed += msg.next
                self.next = 7 + 11 + parsed

        return


    def compute(self):

        if self.mid == 4:
            return self.lval

        elif self.mid == 0:
            return sum([x.compute() for x in self.subpackets])
        
        elif self.mid == 1:
            tmp = [ x.compute() for x in self.subpackets ]
            res = 1
            for val in tmp:
                res = res * val
            return res

        elif self.mid == 2:
            return min([x.compute() for x in self.subpackets])

        elif self.mid == 3:
            return max([x.compute() for x in self.subpackets])
        
        elif self.mid == 5:
            ops = [ x.compute() for x in self.subpackets ]
            if ops[0] > ops[1]:
                return 1
            else:
                return 0
        
        elif self.mid == 6:
            ops = [ x.compute() for x in self.subpackets ]
            if ops[0] < ops[1]:
                return 1
            else:
                return 0
        
        elif self.mid == 7:
            ops = [ x.compute() for x in self.subpackets ]
            if ops[0] == ops[1]:
                return 1
            else:
                return 0


def parse_input(text):

    res = []
    lines = [ x for x in text.split("\n") if x != "" ]

    hex_dig = [ int(x, 16) for x in lines[0] ]
    for h in hex_dig:
        res.append(f"{h:04b}")
    res = "".join(res)

    m = Message(res)

    return m


def sum_pkgver(m):

    res = m.ver

    for sb in m.subpackets:
        res += sum_pkgver(sb)

    return res


def compute_expr(m):

    res = None
    

    return



if __name__ == "__main__":

    RES = None

    if os.path.exists(sys.argv[1]):
        FD = open(sys.argv[1])
        TEXT = FD.read()
        FD.close()
    else:
        TEXT = sys.argv[1]

    DATA = parse_input(TEXT)
    RES = sum_pkgver(DATA)
    print("sol01: {}".format(RES))

    RES = DATA.compute()
    print("sol02: {}".format(RES))
