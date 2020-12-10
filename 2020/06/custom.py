#!/usr/bin/python

import sys


def count_distinct(text):

    res = 0
    letter_set = set()
    s = "".join(text)
    for c in s:
        letter_set.add(c)

    #print(letter_set)
    return len(letter_set)


def cl(S,T):

    res = []
    for si in S:
        if si in T:
            res.append(si)
    res = "".join(res)
    return res


def count_cl(grp):


    print("\n=================")
    print(grp)
    grp = ["".join(sorted(g)) for g in grp]
    tmp_s = grp[0]
    for idx, s in enumerate(grp[1:]):
        print("    ", idx, tmp_s, s)
        tmp_s = "".join(list(cl(tmp_s, s)))
    
     
    print("tmp_cl: {}".format(tmp_s))
    return len(tmp_s)




fd = open(sys.argv[1])
text = fd.read()
fd.close()


groups = text.split("\n\n")
groups = [g for g in groups if g != ""]

parsed_groups = []
for g in groups:
    group = g.split("\n")
    group = [g.strip() for g in group if g != ""]
    parsed_groups.append(group)

#for p in parsed_groups:
#    print(count_distinct(p))

aa = [count_distinct(p) for p in parsed_groups]
print(sum(aa))

#print(aa)
print(parsed_groups[0])
print(count_cl(parsed_groups[0]))


test = [
    ["abc"],
    ["a", "b", "c"],
    ["ab", "ac"],
    ["a", "a", "a", "a"],
    ["b"],
    ]
#
bb = [count_cl(p) for p in parsed_groups]
#bb = [count_cl(p) for p in test]
print(sum(bb))


