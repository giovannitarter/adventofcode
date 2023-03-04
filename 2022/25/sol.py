#!/usr/bin/python


import sys
import copy



def parse_input(text):

    res = None
    lines = [x for x in text.split("\n") if x != ""]
    return lines


SNA_TO_DEC = {
        "=" : -2,
        "-" : -1,
        "0" :  0,
        "1" :  1,
        "2" :  2,
        }
#DEC_TO_SNA = {v:k for k, v in SNA_TO_DEC.items()}
#print(DEC_TO_SNA)

DEC_TO_SNA = {
        0 : "0",
        1 : "1",
        2 : "2",
        3 : "1=",
        4 : "1-",
        }


def to_dec(text):
    digits = list(text)

    res = 0
    for idx, d in enumerate(digits[::-1]):
        res += SNA_TO_DEC[d] * pow(5, idx)

    return res


def to_snafu(dec):

    res = []
    carry = 0
    while dec > 0:
        quo = dec // 5
        rem = dec % 5
        dec = quo

        d = rem + carry
        carry = 0

        if d == 5:
            carry = 1
            res.append("0")
        elif d == 4:
            carry = 1
            res.append("-")
        elif d == 3:
            carry = 1
            res.append("=")

        else:
            res.append(str(d))

    if carry:
        res.append("1")

    res = "".join(res[::-1])

    return res


def sol01(data):
    res = sum([to_dec(x) for x in data])
    res = to_snafu(res)
    return res


def sol02(data):
    res = None
    return res


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

