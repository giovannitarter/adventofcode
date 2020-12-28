#!/usr/bin/python

import sys
import re



def parse_line(line):

    ingredients = re.match(r"(\w* )+\(contains", line)
    ingredients = ingredients.group(0).split()[:-1]
    
    allergenes = re.search(r" \(contains ([\w, ]*)\)", line)
    allergenes = [a.strip() for a in allergenes.group(1).split(",")]

    res = (ingredients, allergenes)
    return res



fd = open(sys.argv[1])
text = fd.read()
fd.close()


lines = text.split("\n")
lines = [l for l in lines if l != ""]

foods = []

alr_to_ing = {}
ing_to_alr = {}

all_ing = set()
all_all = set()

for l in lines:
    #print("")
    #print(l)
    
    food = parse_line(l)
    
    foods.append(food)

    ing, alr = food
    all_ing.update(ing)
    all_all.update(alr)

    for a in alr:

        a_set = alr_to_ing.get(a, set(ing))
        a_set = a_set.intersection(set(ing))
        alr_to_ing[a] = a_set


#containing allergenes
ca = set()
for i in alr_to_ing:
    print("all: {} -> {}".format(i, alr_to_ing[i]))
    ca = ca.union(alr_to_ing[i])

not_ca = all_ing - ca

sol1 = 0
for ing, alr in foods:  
    for i in ing:
        if i in not_ca:
            sol1 = sol1 + 1

print("SOL1: {}".format(sol1))

print(ca)
