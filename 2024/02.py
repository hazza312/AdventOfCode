from typing import List

from common import run_day


def gap_is_ok(gap):
    return 1 <= abs(gap) <= 3

def is_safe(row):
    gap = row[1] - row[0]
    if not gap_is_ok(gap):
        return False

    for a, b in zip(row[1:], row[2:]):
        new_gap = b - a
        if not gap_is_ok(new_gap):
            return False
        if gap // abs(gap) != new_gap // abs(new_gap):
            return False

        gap = new_gap

    return True

def is_safe_with_removing(row: List[int]):
    if is_safe(row):
        return True

    for i in range(len(row)):
        modified = list(row)
        modified.pop(i)
        if is_safe(modified):
            return True

    return False

def main(f):
    part1_count = 0
    part2_count = 0
    for line in f:
        line = list(map(int, line.split()))
        part1_count += is_safe(line)
        part2_count += is_safe_with_removing(line)

    print(part1_count)
    print(part2_count)

if __name__ == '__main__':
    run_day(2, main)
