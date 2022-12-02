#!/usr/bin/python


import sys
import copy



def parse_input(text):
    res = [tuple(x.split()) for x in text.split("\n") if x != ""]
    return res


def decrypt(val):

    dec_map = {
        "X" : "A",
        "Y" : "B",
        "Z" : "C",
        }
    return dec_map[val]


def decrypt_game(game):
    return [(m1, decrypt(m2)) for m1, m2 in game]


def score(m1, m2):

    shape_score = {
            "A" : 1,
            "B" : 2,
            "C" : 3,
        }

    # A : Rock
    # B : Paper
    # C : Scissor

    vs_score = {
            ("A", "A") : (3, 3),
            ("A", "B") : (0, 6),
            ("A", "C") : (6, 0),

            ("B", "A") : (6, 0),
            ("B", "B") : (3, 3),
            ("B", "C") : (0, 6),

            ("C", "A") : (0, 6),
            ("C", "B") : (6, 0),
            ("C", "C") : (3, 3),
        }

    r1 = shape_score[m1]
    r2 = shape_score[m2]
    s1, s2 = vs_score[(m1, m2)]
    r1 = r1 + s1
    r2 = r2 + s2
    return((r1, r2))


def sol01(game):

    acc = 0
    for round in game:
        acc += score(*round)[1]

    return acc


def sol02(game):

    # A : Rock
    # B : Paper
    # C : Scissor

    # X: lose
    # Y: draw
    # Z: win

    lose = {
            "A" : "B",
            "B" : "C",
            "C" : "A",
            }

    win = {
            "A" : "C",
            "B" : "A",
            "C" : "B",
            }

    pts_choose = {
            "A" : 1,
            "B" : 2,
            "C" : 3,
        }

    pts_round = {
            "X" : 0,
            "Y" : 3,
            "Z" : 6,
        }

    score = 0
    for opp, res in game:

        if res == "X":
            mov = win[opp]
        elif res == "Y":
            mov = opp
        elif res == "Z":
            mov = lose[opp]

        score += pts_round[res]
        score += pts_choose[mov]

    return score


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)
    DEC_DATA = decrypt_game(DATA)

    SOL01 = sol01(DEC_DATA)
    print("sol01 : {}".format(SOL01))

    SOL02 = sol02(DATA)
    print("sol02 : {}".format(SOL02))


