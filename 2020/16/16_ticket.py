#!/usr/bin/python

import sys
import re


def parse_file(lines):

    ticket_start = lines.index("your ticket:")
    nearby_start = lines.index("nearby tickets:", ticket_start)

    rules_lines = lines[:ticket_start]
    my_ticket = lines[ticket_start:nearby_start][1:]
    nearby = lines[nearby_start:][1:]

    rules = []
    for r in rules_lines:
        #print(r)
        m = re.match(r"([\w ]*): (\d*)-(\d*) or (\d*)-(\d*)", r)
        rules.append(m.groups())

    my_ticket = [int(x) for x in my_ticket[0].split(",")]
    nearby_str = [x.split(",") for x in nearby]

    nearby = []
    for n in nearby_str:
        nearby.append([int(x) for x in n])

    return(rules, my_ticket, nearby)


def check_ticket(ticket, rule):

    rule_val = [int(x) for x in list(rule[1:])]

    invalid_nr = []

    for t in ticket:

        valid_nr = False
        for ri in range(0, len(rule_val), 2):

            cmin = rule_val[ri]
            cmax = rule_val[ri + 1]

            if t >= cmin and t <= cmax:
                valid_nr = True
                break

        if not valid_nr:
            invalid_nr.append(t)

    return invalid_nr


def check_column(column, rules):
    """
    returns the list of compatible columns
    """
    
    res = []

    for r in rules:
        c_inv = check_ticket(column, r)
        if len(c_inv) == 0:
            res.append(r[0])

    return res


##########################################
# MAIN
#########################################

fd = open(sys.argv[1])
text = fd.read()
fd.close()

lines = text.split("\n")
lines = [l for l in lines if l != ""]

rules, my_ticket, nearby = parse_file(lines)

#print("\nrules")
#print(rules)

print("\nmy_ticket")
print(my_ticket)

print("\nnearby {}".format(len(nearby)))
#print(nearby)

valid_tickets = []

acc = []
for n in nearby:

    #print("\nticket: {}".format(n))
    invalid = set(n)
    for r in rules:
        c_inv = check_ticket(n, r)
        invalid = invalid.intersection(c_inv)

    acc.extend(list((invalid)))

    if len(invalid) == 0:
        valid_tickets.append(n)

#print(acc)
print("SOL1: {}".format(sum(acc)))

print("valid tickets nr: {}".format(len(valid_tickets)))




transp = list(zip(* valid_tickets))
ctable = {}
for ci, c in enumerate(transp):
    comp = check_column(c, rules)
    ctable[ci] = comp

#print(ctable)


res = {}
cat = [x[0] for x in rules]
cols = ctable.keys()

#assigning columns to categories (max 1 col matching a category)
while len(cat) > 0:
    for ci in ctable:
        
        ccat = ctable[ci] 
        if len(ccat) == 1:

            assigned = ccat[0]
            print("assigned \"{}\" to {}".format(assigned, ci))

            res[assigned] = ci
            cat.remove(ccat[0])

            for c in ctable:
                if assigned in ctable[c]:
                    ctable[c].remove(assigned)

print(res)

acc = []
for cat in res:
    if cat.startswith("departure"):
        acc.append(my_ticket[res[cat]])
#print(acc)

sol2 = 1
for a in acc:
    sol2 = sol2 * a
print("SOL2: {}".format(sol2))


#print("col {} compatible with {}".format(ci, comp))






