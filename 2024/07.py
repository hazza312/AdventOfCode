from operator import add, mul

from common import run_day

def concat(a, b):
    return int(str(a) + str(b))

def can_make_target(target, curr, row, ops=(add, mul)):
    if len(row) == 0:
        return curr == target

    for op in ops:
        if can_make_target(target, op(curr, row[0]), row[1:], ops=ops):
            return True

    return False

def main(f):
    part1_sum = 0
    part2_sum = 0
    for line in f:
        target, row = line.split(":")
        target = int(target)
        row = [int(n) for n in row.split()]

        part1_sum += target * can_make_target(target, 0, row)
        part2_sum += target * can_make_target(target, 0, row, ops=(add, mul, concat))

    print(part1_sum)
    print(part2_sum)


if __name__ == '__main__':
    run_day(7, main)
