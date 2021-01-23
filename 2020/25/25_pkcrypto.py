#!/usr/bin/python

import sys



SUBJECT_NR = 7
CONST=20201227

def compute_public_key(loop_size, subject_nr):

    val = 1
    for i in range(loop_size):
        val = val * subject_nr
        val = val % CONST
    return val


def find_loop_size(pk, subject_nr=SUBJECT_NR):
    
    res = None

    lz = 1
    val = 1
    while res is None:

        #if lz % 10000 == 0:
        #    print(lz)

        val = val * subject_nr
        val = val % CONST
        
        if val == pk:
            res = lz
            break

        lz = lz + 1
        
    return res


fd = open(sys.argv[1])
text = fd.read()
fd.close()


lines = text.split("\n")
lines = [l for l in lines if l != ""]


card_pk = int(lines[0])
door_pk = int(lines[1])

print("card pk: {}".format(card_pk))
print("door pk: {}".format(door_pk))

#card_pk = compute_public_key(8, 7)
#print(card_pk)

card_lz = find_loop_size(card_pk, 7)
print("card lz: {}".format(card_lz))

door_lz = find_loop_size(door_pk, 7)
print("door_lz: {}".format(door_lz))

if card_lz is None or door_lz is None:
    sys.exit(1)

card_ek = compute_public_key(card_lz, door_pk)
door_ek = compute_public_key(door_lz, card_pk)

print("card ek: {}".format(card_ek))
print("door_ek: {}".format(door_ek))




