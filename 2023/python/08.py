import sys
import re
from itertools import cycle
from math import lcm


def read_network():
    network = {}
    for line in sys.stdin:
        src, left, right = re.match(r'(\w+) = \((\w+), (\w+)\)', line).groups()
        network[src] = (left, right)

    return network


def path_length(net, pattern, start, reached_end):
    curr = start
    for step, direction in enumerate(cycle(pattern), start=1):
        curr = net[curr][0 if direction == 'L' else 1]

        if reached_end(curr):
            return step


def path_length_simultaneous(net, pattern):
    path_lengths = [
        path_length(net, pattern, s, lambda x: x.endswith('Z'))
        for s in net.keys() if s.endswith('A')
    ]

    return lcm(*path_lengths)


if __name__ == '__main__':
    pattern = sys.stdin.readline().strip()
    sys.stdin.readline()
    net = read_network()

    print(path_length(net, pattern, start='AAA', reached_end=lambda x: x == 'ZZZ'))
    print(path_length_simultaneous(net, pattern))
