#!/usr/bin/python


import sys
import copy
import re



def parse_input(text):
    text = text.replace("\n", "")
    return text.strip().split(",")


def calc_hash(chunk):

    curr = 0
    for c in chunk.encode("ascii"):
        curr = ((curr + c) * 17) % 256

    return curr


def sol01(data):
    return sum([calc_hash(d) for d in data])


def find_label(box, label):
    for idx, (item_lbl, focal_len) in enumerate(box):
        if item_lbl == label:
            return idx

    return -1


def print_boxes(boxes):

    for b, v in sorted(boxes.items()):
        if v:
            print(f"{b} -> {v}")
    return


def sol02(data):

    boxes = {i:[] for i in range(256)}
    for idx, d in enumerate(data):

        m = re.match(r"([a-z]+)([=-])([\d]*)", d)
        label, op, lens_nr = m.groups()

        box = boxes[calc_hash(label)]
        lbl_pos = find_label(box, label)
        if op == "=":
            if lbl_pos != -1:
                box[lbl_pos] = (label, lens_nr)
            else:
                box.append((label, lens_nr))

        elif op == "-":
            if lbl_pos != -1:
                box.pop(lbl_pos)

    res = []
    for b, v in boxes.items():
        for idx, (lbl, lnr) in enumerate(v):
            res.append((b+1) * (idx+1) * int(lnr))


    return sum(res)


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)
    #print(f"DATA:\n{DATA}\n")

    SOL01 = sol01(DATA)
    print("SOL01: {}".format(SOL01))

    SOL02 = sol02(DATA)
    print("SOL02: {}".format(SOL02))

