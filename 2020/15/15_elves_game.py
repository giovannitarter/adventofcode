#!/usr/bin/python

import sys


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

print(seq)

print("")

#spoken = {}
#for i, s in enumerate(test[:-1]):
#    spoken[s] = [i + 1]
#spk = test[-1]
#
#turn = len(seq) + 1
#
#while turn < 15:
#
#    last = seq[-1]
#    print("\nturn: {}, last: {}".format(turn, last))
#    print(seq)
#    print(spoken)
#    
#    apparition = spoken.get(last)
#    if apparition is None:
#        spk = 0
#    else:
#        spk = apparition[-1] - apparition[-2]
#
#    seq.append(spk)
#
#
#    print("turn: {} spk: {}".format(turn, spk))
#
#    turn = turn + 1


#SOL1


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

print(number_at(seq, 2020))
print(number_at(seq, 30000000))








