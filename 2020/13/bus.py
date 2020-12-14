#!/usr/bin/python

import sys


fd = open(sys.argv[1])
text = fd.read()
fd.close()


lines = text.split("\n")
lines = [l for l in lines if l != ""]

#for l in lines:
#    print(l)

min_depart = int(lines[0])

bus_nr = []
for br in lines[1].split(","):
    if br != "x":
        bus_nr.append(int(br))

print(min_depart)
print(bus_nr)

mod_bus_nr = [x - (min_depart % x) for x in bus_nr]

next_bus_scat = min(mod_bus_nr)
next_bus = (bus_nr[mod_bus_nr.index(next_bus_scat)])

print(next_bus_scat)
print(next_bus)
print(next_bus_scat * next_bus)


