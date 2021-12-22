#!/usr/bin/python


import sys
import copy
import os


class Tree():

    def __init__(self, sf_nr, parent=None):
        
        self.parent = parent
        if isinstance(sf_nr, int):
            self.value = sf_nr
            self.left = None
            self.right = None

        elif isinstance(sf_nr, list):
            if isinstance(sf_nr[0], Tree) and isinstance(sf_nr[1], Tree):
                self.value = None
                self.left = sf_nr[0]
                self.right = sf_nr[1]
                self.left.parent = self
                self.right.parent = self

            else:
                self.value = None
                self.left = Tree(sf_nr[0], self)
                self.right = Tree(sf_nr[1], self)


    def get_sf_number(self):

        if self.value is None:
            res = [self.left.get_sf_number(), self.right.get_sf_number()]
        else:
            res = self.value        
        
        return res


    def find_splittable(self):
        
        if self.value is not None:
            if self.value >= 10:
                return self
            else:
                return None
        
        else:
            res = self.left.find_splittable()
            if res is None:
                res = self.right.find_splittable()

            return res


    def split(self):

        res = False
        
        c = self.find_splittable()
        if c is not None:
            #print(f"splitting {c.get_sf_number()}")
            c.left = Tree(c.value // 2, c)
            c.right = Tree(-(c.value // -2), c)
            c.value = None

            res = True
        
        return res
    

    def find_tbexploded(self, lev=0):
        
        if self.value is None:
            
            if lev >= 4:
                return self

            res = self.left.find_tbexploded(lev+1)
            
            if res is None:
                res = self.right.find_tbexploded(lev+1)

            return res

    
    def first_rn_left(self):

        if self.value is not None:
            return self
        else:
            return self.left.first_rn_left()
    
    
    def first_rn_right(self):

        if self.value is not None:
            return self
        else:
            return self.right.first_rn_right()

    
    def succ_right(self):

        res = None
        par = self.parent
        last_node = self

        while par != None and res is None:
            
            if par.right != last_node:
                res = par.right.first_rn_left()
            
            last_node = par
            par = par.parent

        return res
    

    def pred_left(self):

        res = None
        par = self.parent
        last_node = self

        while par != None and res is None:

            if par.left != last_node:
                res = par.left.first_rn_right()
            
            last_node = par
            par = par.parent

        return res


    def explode(self):
    
        res = False
        c = self.find_tbexploded()
        
        if c is not None:
            #print(f"exploding: {c.get_sf_number()}")
            
            sr = c.succ_right()
            pl = c.pred_left()
            
            #print(f"sr: {sr.get_sf_number()}")
            #print(f"pl: {pl.get_sf_number()}")
            
            if sr is not None:
                sr.value += c.right.value

            if pl is not None:
                pl.value += c.left.value

            
            c.value = 0
            c.left = None
            c.right = None
    
            res = True
        return res


    def reduce_sf(self):
        while True:

            exp = self.explode()
            #print(f"exp: {self.get_sf_number()}")
            if not exp:
                spl = self.split()
                #print(f"spl: {self.get_sf_number()}")
                if not spl:
                    break


    def sum(self, b):
        res = Tree([self, b], None)
        
        #print("")
        #print(f"red: {res.get_sf_number()}")
        res.reduce_sf()
        return res
 

    def magnitude(self):

        if self.value is not None:
            return self.value
        else:
            return 3 * self.left.magnitude() + 2 * self.right.magnitude() 


def parse_input(text):

    res = [ eval(x) for x in text.split("\n") if x != "" ]
    return res


if __name__ == "__main__":

    RES = None

    if os.path.exists(sys.argv[1]):
        FD = open(sys.argv[1])
        TEXT = FD.read()
        FD.close()
    else:
        TEXT = "\n".join(sys.argv[1:])
        

    DATA = parse_input(TEXT)
    #print(DATA[0])
    
    t = Tree(DATA[0])
    
    for d in DATA[1:]:
        #print("")
        #print(f"a: {t.get_sf_number()}")
        b = Tree(d)
        #print(f"b: {b.get_sf_number()}")
        t = t.sum(b)

    #print(f"reduced sum: {t.get_sf_number()}")
    RES = t.magnitude()

    print("\nsol01: {}".format(RES))


    RES = 0
    for i, a in enumerate(DATA):
        for j, b in enumerate(DATA):
            if i != j:
                
                oa = Tree(a)
                ob = Tree(b) 
                
                #print(f"\na: {oa.get_sf_number()}\nb: {ob.get_sf_number()}")

                oc = oa.sum(ob)

                mc = oc.magnitude()
                if mc > RES:
                    RES = mc
    
    print("\nsol02: {}".format(RES))

