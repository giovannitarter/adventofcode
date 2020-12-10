#!/usr/bin/python

import sys


fd = open(sys.argv[1])
text = fd.read()
fd.close()


lines = text.split("\n")
lines = [l for l in lines if l != ""]

adapter_set = []
for l in lines:
    adapter_set.append(int(l))



higher = max(adapter_set)
device = higher + 3

adapter_set.append(0)
adapter_set.append(device)

adapter_set = sorted(adapter_set)

print("higher: {}".format(higher))
print("device: {}".format(device))
print(adapter_set)


res = {}

for idx, a in enumerate(adapter_set[:-1]):
    cur = adapter_set[idx]
    nxt = adapter_set[idx + 1]
    diff = nxt - cur
    
    tmp = res.get(diff, 0)
    res[diff] = tmp + 1
    if diff == 2:
        print(cur)

print(res)
print("sol1: {}".format(res[1] * res[3]))

