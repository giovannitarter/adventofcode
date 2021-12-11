#!/usr/bin/python


import sys
import copy


def get_neigh(x, y, max_x, max_y):

    nlist = [
            (-1, -1),
            (0, -1),
            (1, -1),
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0)
            ]

    res = []
    
    for dx, dy in nlist:
        nx = x + dx
        ny = y + dy

        if ( nx > -1 
             and nx < max_x 
             and ny > -1
             and ny < max_y
           ):
            res.append((nx, ny))
    
    return res


def parse_input(text):

    res = []
    lines = [ x for x in text.split("\n") if x != "" ]
    
    for l in lines:
        res.append([int(x) for x in l])

    return res


def update_neigh(x, y, data):

    neighs = get_neigh(x, y, len(data[0]), len(data))
    #print(f"neighs: {neighs}")
    
    for nx, ny in neighs:
        if data[ny][nx] > 0:
            data[ny][nx] = data[ny][nx] + 1

    return


def get_flasher(data):
    """
    return a list of nodes that flash
    """
    res = []

    for y, row in enumerate(data):
        for x, v in enumerate(row):
            if v > 9:
                res.append((x, y))
    
    return res


def print_data(data):
    for d in data:
        print(f"{d}")


def step(data):

    flash_nr = 0
    
    for y, row in enumerate(data):
        for x, v in enumerate(row):
            data[y][x] += 1
    
    flasher = get_flasher(data)
    while len(flasher) > 0:
        
        flash_nr += len(flasher)

        for fx, fy in flasher:
            update_neigh(fx, fy, data)
            data[fy][fx] = 0
         
        flasher = get_flasher(data)

    return data, flash_nr



def sol01(data):
    
    flash_nr = 0
    for i in range(1, 101):
        
        data, fnr = step(data)
        flash_nr += fnr

        #print(f"\nafter step {i}")
        #for d in data:
        #    print(d)
    
    return flash_nr


def check_sync(data):
    
    res = True

    for y, row in enumerate(data):
        for x, v in enumerate(row):
            if v != 0:
                return False

    return True
    

def sol02(data):

    step_nr = 0
    
    while not check_sync(data):
        data, fnr = step(data)
        step_nr += 1

    return step_nr



if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()


    DATA = parse_input(TEXT)
    DATA2 = copy.deepcopy(DATA)
    
    RES = sol01(DATA)
    print(f"sol1: {RES}")
    
    RES = sol02(DATA2)
    print(f"sol2: {RES}")

    





