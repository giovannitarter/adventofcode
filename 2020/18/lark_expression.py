from lark import Lark, Transformer, v_args


calc_grammar = """

    ?start: sum

    ?sum: product
        | sum "+" product   -> add
        | sum "-" product   -> sub

    ?product: atom
        | product "*" atom  -> mul

    ?atom: NUMBER           -> number
         | "-" atom         -> neg
         | "(" sum ")"

    %import common.CNAME -> NAME
    %import common.NUMBER
    %import common.WS_INLINE

    %ignore WS_INLINE
"""


@v_args(inline=True)    # Affects the signatures of the methods
class CalculateTree(Transformer):
    from operator import add, sub, mul, neg
    number = float

calc_parser = Lark(calc_grammar, parser='lalr', transformer=CalculateTree())
calc = calc_parser.parse


def test():
    print(calc("1+5*-3"))
    print(calc("(1+5)*-3"))


if __name__ == '__main__':
     test()
    #main()
