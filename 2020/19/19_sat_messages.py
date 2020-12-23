#!/usr/bin/python

import sys
import re


TERM = r"tr"
OR = r"or"
LIST = r"ls"
LOOP = r"lp"


def parse_lines(lines):

    strings_start = lines.index("")
    rules_lines = lines[:strings_start]
    strings = lines[strings_start+1:]

    strings = [s for s in strings if s != ""]


    rules = {}
    for r in rules_lines:

        if (m := re.match("(\d*): \"(\w*)\"", r)) is not None:
            rules[int(m.group(1))] = (TERM, m.group(2), None)

        elif (idx := r.find(" |")) != -1:
            m = re.match("(\d*): ", r)
            bef = [int(x) for x in r[m.end():idx].split(" ")]
            aft = [int(x) for x in r[idx+3:].split(" ")]

            idx = int(m.group(1))

            loop = False
            if idx in bef:
                loop = True
            elif idx in aft:
                loop = True

            if loop == False:
                rules[int(m.group(1))] = (OR, bef, aft)
            else:
                rules[int(m.group(1))] = (LOOP, bef, aft)

        else:
            m = re.match("(\d*): ", r)
            rules[int(m.group(1))] = (LIST, [int(x) for x in r[m.end():].split(" ")], None)

    return (rules, strings)


def build_regexp(rule_nr, rules):

    tp, arg1, arg2 = rules[rule_nr]

    res = ""

    if tp == TERM:
        res = arg1

    elif tp == LIST:
        tmp = [build_regexp(x, rules) for x in arg1]
        #print("tmp:", tmp)
        res = "".join(tmp)

    elif tp == OR:
        bef = "".join([build_regexp(x, rules) for x in arg1])
        aft = "".join([build_regexp(x, rules) for x in arg2])
        res = "(({})|({}))".format(aft, bef)

    elif tp == LOOP:
        loop_pos = arg2.index(rule_nr)
        bef_loop = arg2[:loop_pos]
        aft_loop = arg2[loop_pos+1:]


        bef = "".join([build_regexp(x, rules) for x in bef_loop])

        aft = "".join([build_regexp(x, rules) for x in aft_loop])

        res = []
        for x in [bef, aft]:
            if len(x) > 0:
                res.append("({})+".format(x))

        res = "".join(res)
        #print(res)

    return res


########################################
# MAIN
#######################################


fd = open(sys.argv[1])
text = fd.read()
fd.close()


lines = text.split("\n")


rules, strings = parse_lines(lines)

print("\nRules:")
for r in sorted(rules.keys()):
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


#PART2

replace = {
    "8:": "8: 42 | 42 8",
    "11:": "11: 42 31 | 42 11 31",
}

lines2 = lines.copy()
for k in replace:
    for i, l in enumerate(lines2):
        if l.startswith(k):
            lines2.pop(i)
            lines2.insert(i, replace[k])


rules2, strings = parse_lines(lines2)
print("\nRules2:")
for r in sorted(rules2.keys()):
    print("{} -> {}".format(r, rules2[r]))

#print("\nStrings:")
#print(strings)

res = build_regexp(0, rules2)
print("\nres", res)

#No way with regex to match an exact number of repetitions!
rex42 = build_regexp(42, rules2)
#rex42 = "^" + rex42
print("\nrex42", rex42)
rex31 = build_regexp(31, rules2)
#rex31 = rex31 + "$"
print("\nrex31", rex31)

print("\n")
acc = 0
for s in strings:
    m = re.fullmatch(res, s)
    #print(s, m)
    if m is not None:

        print("")
        print(s)
        tmp = s
        
        i = 0
        while (m42 := re.match(rex42, tmp)):
            #print(m42)
            tmp = tmp[m42.end():]
            i  += 1
        #print(i)
        #print(tmp)

        #print("m31")
        j = 0
        while (m31 := re.match(rex31, tmp)):
            #print(m31)
            tmp = tmp[m31.end():]
            j += 1
        #print(j)
        print(i, j, "\"{}\"".format(tmp))

        if tmp == "" and i > j:
            acc = acc + 1

print("SOL2")
print(acc)


