from itertools import combinations

from common import run_day

xy = complex

def in_range(p, max_x, max_y):
    return 0 <= p.real <= max_x and 0 <= p.imag <= max_y

def part1(antennae, max_x, max_y):
    antinodes = set()
    for freq, antennae in antennae.items():
        for a, b in combinations(antennae, 2):
            diff = b - a
            antinodes.add(a - diff)
            antinodes.add(b + diff)

    return sum(in_range(p, max_x, max_y) for p in antinodes)


def part2(antennae, max_x, max_y):
    antinodes = set()
    for freq, antennae in antennae.items():
        for a, b in combinations(antennae, 2):
            diff = b - a

            while in_range(a, max_x, max_y):
                antinodes.add(a)
                a -= diff

            while in_range(b, max_x, max_y):
                antinodes.add(b)
                b += diff

    return len(antinodes)

def main(f):
    antennae = {}
    for y, line in enumerate(f):
        for x, c in enumerate(line.strip()):
            if c != '.':
                if c not in antennae:
                    antennae[c] = []

                antennae[c].append(xy(x, y))

    print(part1(antennae, x, y))
    print(part2(antennae, x, y))


if __name__ == '__main__':
    run_day(8, main)
