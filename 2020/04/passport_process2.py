#!/usr/bin/python

import sys
import re


req_fields = {
        "byr" : r"(19[2-9][0-9])|(200[0-2])",
        "iyr" : r"(201[0-9])|(2020)",
        "eyr" : r"(202[0-9])|(2030)",
        "hgt" : r"((1[5-8]\d)|(19[0-3]))cm|((59)|(6\d)|(7[0-6]))in",
        "hcl" : r"#([0-9a-f]{6})",
        "ecl" : r"(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)",
        "pid" : r"\d{9}",
        }
opt_fields = [ "cid" ]


colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


#print(re.match(req_fields["hgt"], "163in"))
#sys.exit(1)


def validate(passport):

    res = True
    for v in req_fields:

        if v not in passport:
            res = False
            break

        res_regexp = None
        res_regexp = re.fullmatch(req_fields[v], passport[v])
        #print("")
        #print("re.match {} {}".format(req_fields[v], passport[v]))

        if res_regexp is None:
            #print(passport[v])
            print("bad field: \"{}\", val: \"{}\", \"{}\"".format(v, passport[v], res_regexp))
            res = False
            break
        else:
            #print("field: \"{}\", val: \"{}\", \"{}\"".format(v, passport[v], res_regexp))
            pass

    return res


def check_range(p, key, mn, mx):

    txt = p[key]
    val = int(txt)
    if val < mn or val > mx:
        return False
    else:
        return True


def check_height(p):

    res = False
    val = p["hgt"]

    unit = val[-2:]
    #print(unit)
    nr = int(val[:-2])
    #print(nr)

    if unit == "cm":
        res = (nr >= 150 and nr <=193)
    elif unit == "in":
        res = (nr >= 59 and nr <=76)

    return res


def check_color(p):
    val = p["ecl"]
    return(val in colors)


def check_digit(p):

    val = p["pid"]

    if len(val) != 9:
        return False

    for i in val:
        if not i.isdigit():
            return False

    return True


fd = open(sys.argv[1])
text = fd.read()
fd.close()

lines = text.split("\n\n")
lines = [ l.replace("\n", " ") for l in lines if l != "" ]
lines = [ l.strip() for l in lines if l != "" ]


ps = []
valid_ps = []
for l in lines:

    passport = {}
    for r in l.split(" "):
        fields = r.split(":")
        f = fields[0]
        v = fields[1]
        passport[f] = v

    ps.append(passport)


valid_ps = [ p for p in ps if validate(p) ]

#second check
for idx, p in enumerate(valid_ps):
    if not check_range(p, "byr", 1920, 2002):
        print("byr")
        print(p)

    if not check_range(p, "iyr", 2010, 2020):
        print("iyr")
        print(p)

    if not check_range(p, "eyr", 2020, 2030):
        print("eyr")
        print(p)

    if not check_height(p):
        print("hgt")
        print(p)

    if not check_color(p):
        print("ecl")
        print(p)

    if not check_digit(p):
        print("pid")
        print(p)

print(len(valid_ps))


