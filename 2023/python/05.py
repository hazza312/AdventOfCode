from functools import reduce
from sys import stdin

import portion as P


def read_maps():
    # maps[i][interval_range] = int_offset_src_to_dst_interval
    maps = []

    while line := stdin.readline():
        if line.isspace():
            stdin.readline()
            maps.append(P.IntervalDict([(P.closed(0, P.inf), 0)]))
        else:
            dst, src, size = map(int, line.split())
            maps[-1][P.closedopen(src, src + size)] = dst - src

    return maps


def evaluate_part_1(seed, maps):
    return reduce(lambda curr, map: curr + map[curr], maps, seed)


def map_interval(interval, map):
    ret = P.empty()
    for sub, offset in map[interval].items():
        ret |= P.closedopen(sub.lower + offset, sub.upper + offset)

    return ret


def evaluate_part2(initial, maps):
    return reduce(lambda curr, map: [map_interval(i, map) for i in curr], maps, initial)


if __name__ == '__main__':
    nums = [int(n) for n in stdin.readline().split()[1:]]
    maps = read_maps()

    print(min(evaluate_part_1(s, maps) for s in nums))

    input_intervals = [P.closedopen(a, a + b) for a, b in zip(nums[::2], nums[1::2])]
    final_intervals = evaluate_part2(input_intervals, maps)
    print(min(x.lower for x in final_intervals if x.lower > 0))  # hack
