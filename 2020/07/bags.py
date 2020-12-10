#!/usr/bin/python

import sys
import re



def parse_line(l):

    #tks = re.match("\w \w bag contain \d+ (\w \w bags,)* (\d+ \w \w bags.)", l)
    tks = re.match(r"(\w+ \w+) bags contain ", l)
    node_name = tks.groups()[0]
    #print(node_name)

    contents = []
    l = l[tks.end(0):]

    for i in re.finditer(r"(\d+) (\w+ \w+) bag(s)*(,|.) *", l):
        print(i.groups())
        contents.append(i.groups()[0:-1])

    return (node_name, contents)




fd = open(sys.argv[1])
text = fd.read()
fd.close()


lines = text.split("\n")
lines = [l for l in lines if l != ""]

#test = "striped turquoise bags contain 1 shiny gold bag, 4 shiny turquoise bags."
#print(parse_line(test))
#sys.exit(1)

#lines = lines[:1]

contains = {}
is_contained = {}

for l in lines:
    #print(l)
    
    name, cont = parse_line(l)
    cont = [c[1] for c in cont]
    contains[name] = cont

    if name not in is_contained:
        is_contained[name] = []

    for c in cont:
        lst = is_contained.get(c, [])
        lst.append(name)
        is_contained[c] = lst


#for idx, r in enumerate(sorted(contains)):
#    print("{}. {} -> {}".format(idx, r, contains[r]))
#
#for idx, r in enumerate(sorted(is_contained)):
#    print("{}. {} -> {}".format(idx, r, is_contained[r]))


arg = "shiny gold"
#arg = "pale white"


#for c in contains:
#    if arg in contains.get(c, []):
#        print(c)

def walk(curr, acc):
    
    #print("")
    #print("====================")
    
    work = is_contained.get(curr, [])
    #print(curr)
    #print(work)

    for c in work:
        walk(c, acc)
        acc.add(c)
    return

#print(is_contained.get(arg, ""))

print(len(contains))
print(len(is_contained))

aa = [c for c in is_contained if len(is_contained[c]) == 0]
print("not containing: {}".format(len(aa)))

all_colors = set()
walk(arg, all_colors)
print(len(all_colors))
#
print(sorted(all_colors))
