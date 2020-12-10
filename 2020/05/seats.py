#!/usr/bin/python

import sys


def to_number(seat_id):

    seat_id = seat_id.replace("F", "0")
    seat_id = seat_id.replace("B", "1")
    
    seat_id = seat_id.replace("L", "0")
    seat_id = seat_id.replace("R", "1")

    row = seat_id[0:7]
    row = int(row, base=2)

    col = seat_id[7:10]
    col = int(col, base=2)

    #print("row: {}, col: {}".format(row, col))
    usid = row * 8 + col
    return usid


fd = open(sys.argv[1])
text = fd.read()
fd.close()


lines = text.split("\n")
lines = [l for l in lines if l != ""]

seats = []
for l in lines:
    seats.append(to_number(l))

test = [
        "BFFFBBFRRR",
        "FFFBBBFRRR",
        "BBFFBBFRLL"
    ]

for t in test:
    print(to_number(t))

print("max: {}".format(max(seats)))


seats = sorted(seats)
print(seats)
for idx, s in enumerate(seats):
    if (idx + 1 < len(seats)) and (seats[idx + 1] != seats[idx] + 1):
        print(s+1)


