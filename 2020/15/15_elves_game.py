#!/usr/bin/python

import sys


fd = open(sys.argv[1])
text = fd.read()
fd.close()


lines = text.split("\n")
lines = [l for l in lines if l != ""]

seq = [int(x) for x in lines[0].split(",")]
print(seq)


test =  [0, 3, 6]

seq = list(test)
print(seq)

print("")

spoken = {}
for i, s in enumerate(test[:-1]):
    spoken[s] = [i + 1]

turn = len(seq) + 1

while turn < 15:

    last = seq[-1]
    print("\nturn: {}, last: {}".format(turn, last))
    print(seq)
    print(spoken)

    if spoken.get(last) is None:
        spk = 0
        seq.append(spk)
        spoken[spk].append(turn)
    else:
        last_seen = spoken.get(last, [])
        print("last seen: {}".format(last_seen))
        nxt = last_seen[-1] - last_seen[-2]

        a = spoken.get(nxt, [])
        a.append(turn)
        spoken[nxt] = a

        seq.append(nxt)
        spk = nxt

    print("turn: {} spk: {}".format(turn, spk))

    turn = turn + 1
