#!/usr/bin/python


import sys
import re

targets = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        }

for i in range(1, 10):
    targets[str(i)] = str(i)

rev_targets = {k[::-1]: v for k, v in targets.items()}


def find_first(l):
    rxp = "|".join(targets.keys())
    matches = re.findall(rxp, l)
    return targets[matches[0]]


def find_last(l):
    rxp = "|".join(rev_targets.keys())
    matches = re.findall(rxp, l[::-1])
    return rev_targets[matches[0]]


def find_number(l):
    first = find_first(l)
    last = find_last(l)
    return int(first + last)


def parse_input(text):
    return [x for x in text.split("\n") if x != ""]


def sol01(data):
    res = [re.sub(r"[\D]*", "", x) for x in data]
    return sum([int(f"{x[0]}{x[-1]}") for x in res if x])


def sol02(data):

    for d in data:
        nr = find_number(d)
        #print(f"{nr} -> {d}")

    return sum([find_number(d) for d in data])


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)
    #print(f"DATA:\n{DATA}\n")

    #print(find_number("fourdcfour466twonesz"))

    SOL01 = sol01(DATA)
    print("SOL01: {}".format(SOL01))

    SOL02 = sol02(DATA)
    print("SOL02: {}".format(SOL02))

