#!/usr/bin/python

import sys
import re
import copy
import math

bdir = {
        "NORTH" : 0,
        "EAST" : 1,
        "SOUTH" : 2,
        "WEST" :3,
}


def parse_text(text):

    tiles = {}
    for r in re.finditer(r"Tile (\d*):([\.#\n]*)", text):
        tile_nr = r.group(1).strip()
        image = r.group(2).strip()
        image = image.split("\n")
        tiles[tile_nr] = image

    return tiles


def print_tile(tile):

    for i in tile:
        print(i)
    
    return


def nop(image):
    return image


def transp(image):
    #print("transp:", image)
    transp = zip(*image)
    transp = ["".join(x) for x in transp]    
    return transp


def flip_array(arr):
    mid = len(arr) // 2
    res = arr[:mid:-1] + arr[mid::-1]
    return res


def flip_h(image):
    res = [flip_array(x) for x in image] 
    return res


def flip_v(image):
    return flip_array(image)


def rotate_l(image):
    itransp = transp(image)
    res = flip_h(itransp)
    return res


def rotate_r(image):
    itransp = transp(image)
    res = flip_v(itransp)
    return res

def rotate_cw(image, deg):
    res = image
    for i in range(deg // 90):
        res = rotate_r(res)
    return res


def all_transforms(image):

    res = set()

    for rot in [0, 90, 180, 270]:
        for f in [nop, flip_v, flip_h]:
            tmp = copy.deepcopy(image)
            tmp = rotate_cw(f(tmp), rot)
            tmp = "".join(tmp)

            res.add(tmp)
    #print(res)
    
    tmp = []
    for r in res:
        t = []
        for l in range(0, len(r), 10):
            t.append(r[l:l+10])
        tmp.append(t)

    return tmp



def borders(image):
    
    res = []
    itransp = transp(image)
    
    res.append(image[0]) #NORTH
    res.append(itransp[-1]) #EAST
    res.append(image[-1]) #SOUTH
    res.append(itransp[0]) #WEST
    return res


def all_borders(image_list):

    res = set()
    for i in image_list:
        for b in borders(i):
            res.add(b)

    return(list(res))


def check_match(tile1, tile2, mdir):

    if mdir == "RIGHT":
        m1bor = bdir["EAST"]
        m2bor = bdir["WEST"]
    elif mdir == "DOWN":
        m1bor = bdir["SOUTH"]
        m2bor = bdir["NORTH"]


    at2 = all_transforms(tile2)
    b1 = (borders(tile1))[m1bor]
    
    for im2  in at2:
        b2 = (borders(im2))[m2bor]
        if b1 == b2:
            return(im2)

    return 


def build_row(tid, tile, x_nr):
    
    res = [(tid, tile)]

    cid = tid
    ctile = tile

    for x in range(1, x_nr):
        for nid in adj[cid]:
            ntile = tiles[nid]
            mt = check_match(ctile, ntile, "RIGHT")
            if mt is not None:
                #print("found ", nid)
                cid = nid
                ctile = mt
                res.append((cid, ctile))

    return res


def try_build(sid, stile, y_nr):
    print("\ntry_build {}".format(sid))

    cid = sid
    ctile = stile

    print_tile(ctile)

    res = []
    for y in range(y_nr):

        print("")
        print("y: {}, cid {}".format(y, cid))
        print("res: {}".format(res))

        row = build_row(cid, ctile, y_nr)
        trow = [x[0] for x in row]
        print("row:", trow) 
        
        if len(row) != y_nr:
            break
        else:
            res.append(row)

        print("r adj cid {}: {}".format(cid, adj[cid]))
        for nid in adj[cid]:
            
            if nid in [r[0] for r in row]:
                continue

            print("checking down {}".format(nid))
            
            ntile = tiles[nid]
            mt = check_match(ctile, ntile, "DOWN")
            if mt is not None:
                #print("nid", nid)
                cid = nid
                ctile = mt
            else:
                continue

    return res


    #otiles = {
    #        first_tile : stile
    #        }
    #
    ##print("")
    #cid = first_tile
    #    #print("\ny: {}".format(y))
    #    #print("x: 0 {}".format(cid))
    #    
    #    ftl = cid
    #    
    #    #print(adj[ftl])
    #    for nid in adj[ftl]:
    #        
    #        if nid in otiles:
    #            continue
    #        
    #        ntile = tiles[nid]
    #
    #        #print("checking", nid)
    #        #print(mt)
    #        if mt is not None:
    #            cid = nid
    #            otiles[nid] = mt
    #            #print("")
    #        else:
    #            break
    #
    #return otiles



####################################
# MAIN
####################################


fd = open(sys.argv[1])
text = fd.read()
fd.close()

tiles = parse_text(text)

adj = {}
for tid1 in tiles:
    for tid2 in tiles:
        
        if tid1 == tid2:
            continue

        t1 = tiles[tid1]
        t2 = tiles[tid2]

        for b1 in borders(t1):
            if b1 in all_borders(all_transforms(t2)):
                tmp = adj.get(tid1, [])
                tmp.append(tid2)
                adj[tid1] = tmp


print("")
sol1 = 1
corners = []
for a in adj:
    print("{} -> {}".format(a, adj[a]))
    if len(adj[a]) == 2:
        sol1 = sol1 * int(a)
        corners.append(a)
print("SOL1: {}".format(sol1))

print("Corners: {}".format(corners))

image_edge = int(math.sqrt(len(tiles)))
print("Image edge: {}".format(image_edge))


tile_transforms = {}
for t in tiles:
    tile_transforms[t] = all_transforms(tiles[t])


starts = [(c, tile_transforms[c]) for c in corners]
#print(starts)


for sid, s in starts[:1]:
    for t in s:
        
        #for tid, tile in build_row(sid, t, image_edge):
        #    print(tid)
        #    print_tile(tile)

        res = try_build(sid, t, image_edge)
        acc = 0

        for r in res:
            acc += len(r)

        if acc == len(tiles):
            print("Seq found")
            
            for row in res:
                print([x[0] for x in row])
                #for xid, xtile in row:
                #    print("")
                #    print_tile(xtile)

            sys.exit(1)

        
                
#for o in otiles:
#    print("")
#    print_tile(otiles[o])


#print("##################")
#for a in all_transforms(tiles["2473"]):
#    print("")
#    print_tile(a)


