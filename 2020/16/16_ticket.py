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
print("SUM1: {}".format(sum(acc)))

print("valid tickets nr: {}".format(len(valid_tickets)))

categories = [x[0] for x in rules]
print(categories)



print(rules)


transp = list(zip(* valid_tickets))
for ti, t in enumerate(transp):

    res = {}
    tmp_rules = list(rules)
    for r in rules:
        c_inv = check_ticket(t, r)
        if len(c_inv) == 0:
            print(r[0], ti)






