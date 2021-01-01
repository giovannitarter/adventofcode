#!/usr/bin/python

import sys
import re
import copy


def parse_text(text):

    players = {}

    for mt in re.finditer("Player (\d*):\n(\d+\n)*", text):

        deck = [int(x) for x in mt.group(0).split("\n")[1:] if x != ""]
        players[int(mt.group(1))] = deck

    return players


def round(players):

    res = {}

    drawns = {}
    for p in players:
        drawns[players[p].pop(0)] = p

    max_card = max(drawns.keys())
    winner = drawns[max_card]

    players[winner].append(max_card)
    drawns.pop(max_card)

    for d in drawns:
        players[winner].append(d)

    return winner, players


def print_players(players):
    #print("")
    for p in players:
        print("Player {}'s deck: {}".format(p, ", ".join([str(x) for x in players[p]])))


def keep_playing(players):

    for p in players:
        if len(players[p]) == 0:
            return False

    return True


def get_winner(players):

    res = None

    for p in players:
        if len(players[p]) > 0:
            res = p

    return res


def compute_score(deck):
    res = 0
    for idx, i in enumerate(deck[::-1]):
        res = res + (idx + 1) * i
    return res


def recursive_combat(players, game_nr):

    #returns winner and players

    print("\n\n=== Game {} ===".format(game_nr))

    round_nr = 1
    spawned_games = 1
    mem = set()
    
    while keep_playing(players):
        
        print("\n\n--- Round {} (Game {}) ---".format(round_nr, game_nr))
        print_players(players)

        key = []
        for p in sorted(players):
            tmp_key = ",".join([str(x) for x in players[p]])
            key.append(tmp_key)
        key = tuple(key)
            
        if key in mem:
            print("cards already seen")
            return (1, players)
        else:
            mem.add(key)


        drawns = {}
        sub_check = True
        
        for p in players:
            d = players[p].pop(0)
            drawns[p] = d
            print("Player {} plays: {}".format(p, d))
            #print(len(players[p]))
            if len(players[p]) < d:
                #print("sub_check False")
                sub_check = False

        if sub_check:
            print("Playing a sub-game to determine the winner...")
            
            sub_players = {}
            for p in players:
                sub_players[p] = list(players[p][0:drawns[p]])

            print(drawns)
            print_players(players)
            print_players(sub_players)
            #sys.exit(1)
            
            winner, _ = recursive_combat(sub_players, game_nr + spawned_games)
            print("\n...anyway, back to game {}".format(game_nr))

            spawned_games += 1
            players[winner].append(drawns.pop(winner))
            for p in drawns:
                players[winner].append(drawns[p])

        else:

            for p in players:
                players[p].insert(0, drawns[p])
            winner, players = round(players)
            print("Player {} wins round {} of game {}!".format(winner, round_nr, game_nr))
        
        round_nr += 1
    
    winner = get_winner(players)
    print("The winner of game {} is player {}!".format(
        game_nr, 
        winner
        ))
    return (winner, players)


##################################
# MAIN
#################################

fd = open(sys.argv[1])
text = fd.read()
fd.close()


lines = text.split("\n")
lines = [l for l in lines if l != ""]


initial_players = parse_text(text)
players = copy.deepcopy(initial_players)

#round_nr = 0
#while keep_playing(players):
#    #print_players(players)
#    _, players = round(players)
#    round_nr = round_nr + 1
#
#winner = get_winner(players)
#winner_deck = players[winner]
#sol1 = compute_score(winner_deck)
#print("\nSOL1: {}".format(sol1))


#Recursive combat
mem = {}
players = copy.deepcopy(initial_players)
round_nr = 0

print("\n\nInitial")
print_players(players)

print("")
game_nr = 1
winner, players = recursive_combat(players, 1)

print("winner: {}".format(winner))
print_players(players)

winner = get_winner(players)
winner_deck = players[winner]
sol2 = compute_score(winner_deck)
print("\nSOL2: {}".format(sol2))

