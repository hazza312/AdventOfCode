from collections import Counter

from common import run_day


def count_stones(start, num_blinks):
    curr = Counter(start)
    for _ in range(num_blinks):
        next = Counter()
        for val, qty in curr.items():
            if val == 0:
                next[1] += qty
            elif (l := len(item_str := str(val))) % 2 == 0:
                next[int(item_str[:l // 2])] += qty
                next[int(item_str[l // 2:])] += qty
            else:
                next[val * 2024] += qty
        curr = next

    return curr.total()

def main(f):
    start = [int(n) for n in f.read().split()]
    print(count_stones(start, 25))
    print(count_stones(start, 75))

if __name__ == '__main__':
    run_day(11, main)
