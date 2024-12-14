import operator
import re
from functools import reduce
from math import isclose
from statistics import stdev
from time import sleep

from common import run_day

xy = complex

WIDTH = 101
HEIGHT = 103

def robot_locator(x, y, vx, vy):
    def locator(t):
        return xy((x + t * vx) % WIDTH, (y + t * vy) % HEIGHT)

    return locator

def quadrant(p):
    if p.real == (WIDTH - 1) // 2 or p.imag == (HEIGHT - 1) // 2:
        return None

    w = p.real // (WIDTH / 2)
    h = p.imag // (HEIGHT / 2)
    return int(w * 2 + h)

def get_count_per_quadrant(locs):
    quadrants = [0] * 4
    for loc in locs:
        if (q := quadrant(loc)) is not None:
            quadrants[q] += 1

    return quadrants

def part1(locators):
    locs = [locator(t=100) for locator in locators]
    return reduce(operator.mul, get_count_per_quadrant(locs), 1)

def part2(locators):
    for i in range(10_000):
        locs = set(locator(i) for locator in locators)
        counts = get_count_per_quadrant(locs)
        # trial and error of threshold, expect less dispersion in x-axis
        s = stdev([l.real for l in locs])
        if not isclose(s, 29.2, abs_tol=3):
            print(f"t={i}", counts, s)
            for y in range(HEIGHT):
                print(''.join('*' if xy(x, y) in locs else ' ' for x in range(WIDTH)))
            print()
            sleep(0.2)

def main(f):
    pattern = re.compile(r'(-?\d+)')
    locators = [robot_locator(*(int(n) for n in pattern.findall(line))) for line in f]

    print(part1(locators))
    part2(locators)

if __name__ == '__main__':
    run_day(14, main, 'b')
