#!/usr/bin/python

import sys

def parse_line(l):
    return(int(l))


def check_sum_previous(lst, nr):

    res = False
    print("\n=======================")
    print("nr:{}, list:{}".format(nr, lst))

    for i in lst:
        for j in lst:
            if i != j and i + j == nr:
                res = True
                break

    return res


def find_sequence(lst, nr):

    start = 0
    end = 1

    res = []
    while end < len(lst):

        work = lst[start:end]
        print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("working on: {}".format(work))
        check = sum(lst[start:end])
        
        if check == nr:
            print("found!")
            print(work)
            res = work
            break
        
        elif check < nr:
            end = end + 1

        elif check > nr:
            start = start + 1

    return res



preamble = sys.argv[2]
preamble = int(preamble)


fd = open(sys.argv[1])
text = fd.read()
fd.close()


lines = text.split("\n")
lines = [l for l in lines if l != ""]

seq = []
for l in lines:
    nr = parse_line(l)
    seq.append(nr)


#preamble = 5

for idx in range(preamble, len(seq)):
    nr = seq[idx]
    if check_sum_previous(seq[idx-preamble:idx], nr) == False:
        print("first not matching:")
        print(nr)
        break

not_matching = nr
res = find_sequence(seq, not_matching)
print(min(res) + max(res))

print(len(seq))

