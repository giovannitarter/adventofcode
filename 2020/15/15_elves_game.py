#!/usr/bin/python


import sys


def number_at(seq, pos):

    #Most inefficient ever
    #never gonna work with sol2
    #need an hastable as above
    turn = len(seq) + 1

    rev_seq = list(seq)
    rev_seq.reverse()

    while turn < pos + 1:

        if turn % 1000 == 0:
            print(turn)

        #print("\nturn: {}, seq: {}".format(turn, seq))

        last = rev_seq[0]

        if rev_seq.count(last) == 1:
            seq.append(0)
            rev_seq.insert(0, 0)

        else:
            #print(last)
            last_app = rev_seq.index(last)
            #print("last_app: {}".format(last_app))
            last_bef = rev_seq.index(last, last_app + 1)
            #print("last_bef: {}".format(last_bef))
            seq.append(last_bef - last_app)
            rev_seq.insert(0, last_bef - last_app)

        #print("turn: {}, spk: {}".format(turn, seq[-1]))

        turn = turn + 1

    return rev_seq[0]


def number_at_hash(seq, pos):

    turn = len(seq) + 1

    mem = {}
    for i, s in enumerate(seq):
        mem[s] = [i+1]

    while turn < pos + 1:

        if turn % 1000000 == 0:
            print(turn)

        #print("\nturn: {}, seq: {}".format(turn, seq))
        #print("mem: {}".format(mem))

        last = seq[-1]
        apps = mem.get(last, [])

        if len(apps) < 2:
            nxt = 0

        else:
            nxt = apps[-1] - apps[-2]

        seq.append(nxt)
        tmp = mem.get(nxt, [])
        tmp.append(turn)

        if len(tmp) > 2:
            tmp = tmp[-2:]

        mem[nxt] = tmp

        #print("nxt: {}".format(nxt))
        seq.pop(0)

        turn = turn + 1

    return nxt

###########################
#MAIN
###########################

fd = open(sys.argv[1])
text = fd.read()
fd.close()


lines = text.split("\n")
lines = [l for l in lines if l != ""]

seq = [int(x) for x in lines[0].split(",")]
print(seq)


#test =  [0, 3, 6]
#test =  [1, 3, 2]
#seq = list(test)

#print(seq)

print("")


#SOL1



print("")
print("SOL1")
print(number_at(list(seq), 2020))

print("")
print("SOL2")

#seq = test
print(number_at_hash(list(seq), 2020))
print(number_at_hash(seq, 30000000))








