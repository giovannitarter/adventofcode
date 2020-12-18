#!/usr/bin/python

import sys
from lark import Lark, Transformer, v_args


calc_grammar_1 = """

    ?start: expr

    ?expr: atom
        | expr "+" atom  -> add
        | expr "-" atom  -> sub
        | expr "*" atom  -> mul

    ?atom: NUMBER           -> number
         | "-" atom         -> neg
         | "(" expr ")"

    %import common.NUMBER
    %import common.WS_INLINE

    %ignore WS_INLINE
"""


calc_grammar_2 = """

    ?start: expr

    ?expr: expr_prec
        | expr "*" expr_prec -> mul
        | expr "-" expr_prec -> sub

    ?expr_prec: atom
        | expr_prec "+" atom  -> add

    ?atom: NUMBER           -> number
         | "-" atom         -> neg
         | "(" expr ")"

    %import common.NUMBER
    %import common.WS_INLINE

    %ignore WS_INLINE
"""


@v_args(inline=True)    # Affects the signatures of the methods
class CalculateTree(Transformer):
    from operator import add, sub, mul, neg
    number = int


##########################################
# MAIN
##########################################

fd = open(sys.argv[1])
text = fd.read()
fd.close()


lines = text.split("\n")
lines = [l for l in lines if l != ""]


#SOL1
calc_parser_1 = Lark(calc_grammar_1, parser='lalr', transformer=CalculateTree())

acc = []
for l in lines:
    acc.append(calc_parser_1.parse(l))

print(acc)
print("SOL1: {}".format(sum(acc)))


#SOL2
calc_parser_2 = Lark(calc_grammar_2, parser='lalr', transformer=CalculateTree())
calc_parser_tree = Lark(calc_grammar_2, parser='lalr')

acc = []
for l in lines:
    acc.append(calc_parser_2.parse(l))
    print("")
    print(calc_parser_tree.parse(l))

print(acc)
print("SOL2: {}".format(sum(acc)))


