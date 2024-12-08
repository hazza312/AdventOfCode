import re

from common import run_day


def main(f):
    line = f.read()
    pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    print(sum(int(a) * int(b) for a, b in pattern.findall(line)))

    pattern2 = re.compile(r'(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\))')
    total = 0
    do = True
    for action, arg1, arg2 in pattern2.findall(line):
        if action == 'do()':
            do = True
        elif action == "don't()":
            do = False
        elif do:
            total += int(arg1) * int(arg2)

    print(total)

if __name__ == '__main__':
    run_day(3, main)