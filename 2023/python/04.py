import sys
from collections import Counter


def num_set(s):
    return {int(n) for n in s.split()}


def get_points(n):
    return 0 if n == 0 else 2 ** (n - 1)


def parse_line(line):
    num_part = line.split(':')[1].strip()
    return map(num_set, num_part.split(' | '))


if __name__ == '__main__':
    point_sum = 0
    counts = Counter()
    for i, line in enumerate(sys.stdin, start=1):
        mine, winning = parse_line(line)
        num_hits = len(mine & winning)

        point_sum += get_points(num_hits)
        counts[i] = counts.get(i, 0) + 1
        counts.update(dict((j, counts[i]) for j in range(i + 1, i + 1 + num_hits)))

    print(point_sum)
    print(sum(counts.values()))
