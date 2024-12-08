from collections import Counter

from common import run_day


def main(f):
    first = []
    second = []
    for row in f:
        a, b = row.split()
        first.append(int(a))
        second.append(int(b))

    first.sort()
    second.sort()

    print(sum(abs(b - a) for a, b, in zip(first, second)))

    multipliers = Counter(second)
    print(sum(a * multipliers.get(a, 0) for a in first))

if __name__ == '__main__':
    run_day(1, main)
