#!/usr/bin/python

import sys
import re
import copy



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



#1to1 = {}

def check_all_single(lst):

    for a in lst:
        if len(lst[a]) > 1:
            return False
    
    return True


while check_all_single(alr_to_ing) == False:

    for a in alr_to_ing:
        
        if len(alr_to_ing[a]) == 1:
            
            single = list(alr_to_ing[a])[0]
            #print("single:", single)
            
            for b in alr_to_ing:
                
                if b == a:
                    continue
                
                alr_set = alr_to_ing[b]
                if single in alr_set:
                    alr_set.remove(single)
    

#containing allergenes
ca = set()
for i in alr_to_ing:
    print("all: {} -> {}".format(i, alr_to_ing[i]))
    ca = ca.union(alr_to_ing[i])

#not containing allergenes
not_ca = all_ing - ca

sol1 = 0
for ing, alr in foods:  
    for i in ing:
        if i in not_ca:
            sol1 = sol1 + 1

print("")
print("SOL1: {}".format(sol1))

#print(ca)

for a in alr_to_ing:
    alr_to_ing[a] = alr_to_ing[a].pop()

ing_to_alr = {v: k for k, v in alr_to_ing.items()}


sol2 = []
for i in sorted(ca, key=lambda x: ing_to_alr[x]):
    sol2.append(i)

sol2 = ",".join(sol2)
print("SOL2: {}".format(sol2))
