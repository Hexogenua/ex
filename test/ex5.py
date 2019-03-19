from itertools import product

def expr(p):
    return "{}1{}2{}3{}4{}5{}6{}7{}8{}9".format(*p)


def gen():
    op = ['+', '-','']
    return [expr(p) for p in product(op, repeat=9) if p[0] != '+']

def sum(val):
    for s in filter(lambda x: x[0] == val, map(lambda x: (eval(x), x), gen())):
        print(s)

sum(100)


