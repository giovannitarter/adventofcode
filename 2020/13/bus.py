#!/usr/bin/python

import sys


#https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6

from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod



def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


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



n = [7, 13, 59, 31, 19 ]
a = [0, 1, 4, 6, 7]

print("crt")
print(chinese_remainder(n, a))
