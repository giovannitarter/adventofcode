#!/usr/bin/python


import sys
import copy
import itertools


dig_to_seg = {

        "0" : "abcefg",
        "1" : "cf",
        "2" : "acdeg",
        "3" : "acdfg",
        "4" : "bcdf",
        "5" : "abdfg",
        "6" : "abdefg",
        "7" : "acf",
        "8" : "abcdefg",
        "9" : "abcdfg"
    }

all_seg = dig_to_seg["8"]
all_dig = list(dig_to_seg.keys())


def pat_intesect(pat_a, pat_b):
    return len(set(pat_a).intersection(set(pat_b)))

adj_mat_int = {}
for i in dig_to_seg.keys():
    for j in dig_to_seg.keys():
        adj_mat_int[(i, j)] = pat_intesect(dig_to_seg[i], dig_to_seg[j])

segnr_to_dig = {}
for i in dig_to_seg:
    seg_nr = len(dig_to_seg[i])
    dig_list = segnr_to_dig.get(seg_nr, [])
    dig_list.append(i)
    segnr_to_dig[seg_nr] = dig_list



def get_seq(text):
    text = text.strip()
    text = text.split()
    return text


def sort_string(txt):
    res = "".join(sorted(list(txt)))
    return res


def parse_input(lines):

    res = []
    for l in lines:

        patterns, digits = [get_seq(x) for x in l.split("|")]
        res.append((patterns, digits))

    return res


rules = {

        "1" : lambda x : len(x) == 2,
        "4" : lambda x : len(x) == 4,
        "7" : lambda x : len(x) == 3,
        "8" : lambda x : len(x) == 7,
}


def apply_rules(digit):

    for r in rules:
        res = rules[r](digit)
        if res:
            break

    return res


def sol01(digits):

    count = 0
    for d in digits:
        if apply_rules(d):
            count = count + 1

    return count


def print_mapping(seg_map):

    for s in seg_map:
        print("{} -> {}".format(s, sorted(seg_map[s])))
    return


def verify_assignment(pmap):

    res = True
    for dig_a, pat_a in pmap.items():
        for dig_b, pat_b in pmap.items():
            if pat_intesect(pat_a, pat_b) != adj_mat_int[(dig_a, dig_b)]:
                return False

    return res


def all_mappings(A, B):

    res = []

    for pb in itertools.permutations(B):

        new_map = {}
        for idx, a in enumerate(A):
            new_map[a] = pb[idx]
        res.append(new_map)

    return res


def dict_merge_mappings(A, B):
    """
    A -> list of dicts
    B -> list of dicts
    """

    res = []
    for a in A:
        for b in B:
            r = dict(a)
            r.update(b)
            res.append(r)

    return res


def build_solutions(pat_to_dig, not_assigned):

    base = {}
    for p in pat_to_dig:
        if len(pat_to_dig[p]) == 1:
            base[pat_to_dig[p][0]] = p

    res = [base]
    for dig_na, p_na in not_assigned.items():
        tmp = all_mappings(dig_na, p_na)
        res = dict_merge_mappings(res, tmp)

    return res


def compute_mapping(patterns):

    pat_to_dig = {}
    pox = {}

    for p in patterns:
        plen = len(p)
        pat_to_dig[p] = segnr_to_dig[plen]

        if len(segnr_to_dig[plen]) == 1:
            pass
        else:
            k = tuple(segnr_to_dig[plen])
            a = pox.get(k, [])
            a.append(p)
            pox[k] = a

    csol = build_solutions(pat_to_dig, pox)

    res = []
    for c in csol:
        if verify_assignment(c):
            res.append(c)

    if len(res) > 1:
        print("ERROR")

    tmp = {}
    for k, v in res[0].items():
        v = "".join(sorted(list(v)))
        tmp[v] = k
    res = tmp

    return res


def decode_dig(digits, mapping):

    print(mapping)

    text = []
    for d in digits:
        d = sort_string(d)
        text.append(mapping[d])

    text = "".join(text)
    res = int(text)
    return res


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    LINES = [ x for x in TEXT.split("\n") if x != "" ]

    OBS = parse_input(LINES)

    RES = 0
    for dig_seq in [x[1] for x in OBS]:
        RES += sol01(dig_seq)

    print("res01: {}\n\n".format(RES))

    sol02 = 0
    for mapping, digits in OBS:
        dec_mapping = compute_mapping(mapping)
        nr = decode_dig(digits, dec_mapping)
        sol02 += nr

    print("sol02: {}".format(sol02))

