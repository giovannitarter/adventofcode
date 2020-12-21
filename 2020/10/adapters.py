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



def count_permutations(seq):

    res = 1

    #cstart = 0
    #print("")
    #while cstart < len(seq):

    #    cend = cstart
    #    tmp = []
    #    while cend <= len(seq) and seq[cend] - seq[cstart] <= 4:
    #        tmp.append(seq[cend])
    #        cend = cend + 1
    #    
    #    print(tmp)
    #    cstart = cend - 1

    #for idx, s in enumerate(seq):

    #    if idx < len(seq) - 4:
    #        tmp = seq[idx:idx+5]
    #        diff = tmp[4] - tmp[0]
    #        print(tmp, diff)

    idx = 1
    mul_list = []
    while idx < len(seq) - 1:
       
        print("\nidx: {}, val: {}".format(idx, seq[idx]))
        mul = 1

        if seq[idx + 1] - seq[idx - 1] < 3:
            mul = 2
            
            if (
                    idx+3 < len(seq) 
                    and seq[idx+2] == seq[idx]+2 
                    and seq[idx+1] == seq[idx]+1
                    and seq[idx+3] == seq[idx]+3
               ):
                mul = 7
                idx = idx + 2
            print("next: {}".format(seq[idx]))

            #print("idx: {} -> {} ({})".format(idx, seq[idx], mul))

        mul_list.append(mul)
        print("mul: {}".format(mul))
        res = res * mul
        idx = idx + 1

#    print(mul_list)
    return res



print(adapter_set)

sol2 = count_permutations(adapter_set)

print("\nSOL2:")
print(sol2)





