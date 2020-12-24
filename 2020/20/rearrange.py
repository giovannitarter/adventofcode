#!/usr/bin/python

import sys
import re



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


def flip_array(arr):
    mid = len(arr) // 2
    res = arr[:mid:-1] + arr[mid::-1]
    return res


def flip_h(image):
    res = [flip_array(x) for x in image] 
    return res


def flip_v(image):
    return flip_array(image)


def borders(image):
    
    res = []
    res.append(image[0])
    res.append(image[-1])
    transp = zip(*image)
    transp = ["".join(x) for x in transp]    
    res.append(transp[0])
    res.append(transp[-1])
    return res


def all_transforms(image):

    transforms = [flip_h, flip_v]

    res = [image.copy()]
    
    for t in transforms:
        ci = t(image)
        res.append(ci)

    return res


def all_borders(image_list):

    res = set()
    for i in image_list:
        for b in borders(i):
            res.add(b)

    return(list(res))


def find_neigh(tile_id, tiles):

    res = []
    tile = tiles[tile_id]
    
    brds = all_borders(all_transforms(tile))
    

    
    for ctile in tiles:
        
        if ctile == tile_id:
            continue


        
        cimage = tiles[ctile]
        cbrds = all_borders(all_transforms(cimage))

        for b in brds:
            if b in cbrds:
                res.append(ctile)
                break

    return res



####################################
# MAIN
####################################


fd = open(sys.argv[1])
text = fd.read()
fd.close()


tiles = parse_text(text)
#print(tiles)
#for t in tiles:
#    print_tile(t, tiles)

#print("")
#fst_id = list(tiles.keys())[0]
#arr = tiles[fst][0] + "#"

#fst = tiles[fst_id]
#print(all_transforms(fst))
#for i in all_transforms(fst):
#    print("")
#    print_tile(i)



matches = {}
for tid in tiles:
    n = find_neigh(tid, tiles)
    matches[tid] = n 

acc = []
for m in matches:
    #print(matches[m])

    if len(matches[m]) == 2:
        #print(matches[m])
        acc.append(m)

print(acc)

sol1 = 1
for a in acc:
    sol1 *= int(a)

print("SOL1: {}".format(sol1))



#print("\norig")
#print_tile(fst)
#
#print("\nhoriz")
#print_tile(flip_h(fst))
#
#print("\nvert")
#print_tile(flip_v(fst))


#print_tile(fst)
#print(borders(fst))

#for t in tile 
