import re

import z3

from common import run_day


def solve_tokens_required(ax, ay, bx, by, px, py, offset=0):
    a, b = z3.Ints('a b')
    opt = z3.Optimize()
    opt.add(a * ax + b * bx == px + offset)
    opt.add(a * ay + b * by == py + offset)
    opt.minimize(a * 3 + b)
    if opt.check() != z3.sat:
        return 0

    m = opt.model()
    return m[a].as_long() * 3 + m[b].as_long()


def main(f):
    pattern = re.compile(r'\d+')

    first_total = second_total = 0
    for case in f.read().split('\n\n'):
        params = [int(n) for n in pattern.findall(case)]
        first_total += solve_tokens_required(*params, offset=0)
        second_total += solve_tokens_required(*params, offset=10000000000000)

    print(first_total)
    print(second_total)


if __name__ == '__main__':
    run_day(13, main)
