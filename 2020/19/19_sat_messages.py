#!/usr/bin/python

import sys
import re

fd = open(sys.argv[1])
text = fd.read()
fd.close()


lines = text.split("\n")
#lines = [l for l in lines if l != ""]


strings_start = lines.index("")
rules_lines = lines[:strings_start]
strings = lines[strings_start+1:]

strings = [s for s in strings if s != ""]

TERM = "tr"
OR = "or"
LIST = "ls"

rules = {}
for r in rules_lines:

    if (m := re.match("(\d*): \"(\w*)\"", r)) is not None:
        rules[int(m.group(1))] = (TERM, m.group(2), None)

    elif (idx := r.find(" |")) != -1:
        m = re.match("(\d*): ", r)
        bef = [int(x) for x in r[m.end():idx].split(" ")]
        aft = [int(x) for x in r[idx+3:].split(" ")]
        rules[int(m.group(1))] = (OR, bef, aft)

    else:
        m = re.match("(\d*): ", r)
        rules[int(m.group(1))] = (LIST, [int(x) for x in r[m.end():].split(" ")], None)


def build_regexp(rule_nr, rules):

    #print(rules)

    tp, arg1, arg2 = rules[rule_nr]

    res = ""

    if tp == TERM:
        res = arg1

    elif tp == LIST:
        tmp = [build_regexp(x, rules) for x in arg1]
        print("tmp:", tmp)
        res = "".join(tmp)

    elif tp == OR:
        bef = "".join([build_regexp(x, rules) for x in arg1])
        aft = "".join([build_regexp(x, rules) for x in arg2])
        res = "(({})|({}))".format(aft, bef)

    return res


    #print(m)

print("\nRules:")
for r in rules:
    print("{} -> {}".format(r, rules[r]))

print("\nStrings:")
print(strings)

res = build_regexp(0, rules)
print("\nRES")
print(res)
print("")

acc = 0
for s in strings:
    m = re.fullmatch(res, s)
    #print(s, m)
    if m is not None:
        acc = acc + 1
        #print("matching {}".format(s))

print("SOL1")
print(acc)

#print(rules[0])



