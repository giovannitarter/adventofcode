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



#(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
#32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, (52)
#
#(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
#32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 49, (52)
#
#(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
#32, 33, 34, 35, 38, 39, 42, 45, 46, 48, 49, (52)
#
#(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
#32, 33, 34, 35, 38, 39, 42, 45, 46, 49, (52)
#
#(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
#32, 33, 34, 35, 38, 39, 42, 45, 47, 48, 49, (52)
#
#(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
#46, 48, 49, (52)
#
#(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
#46, 49, (52)
#
#(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
#47, 48, 49, (52)
#
#(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
#47, 49, (52)
#
#(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
#48, 49, (52)



##################################################
#(0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)

test_simple = [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]

def count_permutations(seq, lev=0):

    print("\n") 
    print(" " * lev, "==============================")
    print(" " * lev, seq)

    acc = 1
    for idx in  range(1, len(seq) -1):
        if seq[idx+1] - seq[idx-1] <= 3:
            print(" " * lev, ".. ", seq[idx])
            acc = acc + 2 * count_permutations(seq[idx:], lev+1)

    return acc




print(count_permutations(test_simple))
#print(count_permutations(adapter_set))





