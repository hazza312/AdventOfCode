import sys

DIGIT_MAP = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def get_part1_value(line):
    digits = [int(c) for c in line if c.isdigit()]
    return digits[0] * 10 + digits[-1]


def get_part2_value(line):
    digits = []
    i = 0
    while i < len(line):
        if line[i].isdigit():
            digits.append(int(line[i]))
        else:
            for word, digit in DIGIT_MAP.items():
                if line[i:].startswith(word):
                    digits.append(digit)
                    i += len(word) - 2
                    break
        i += 1

    return digits[0] * 10 + digits[-1]


if __name__ == '__main__':
    part1_sum = part2_sum = 0
    for line in sys.stdin:
        part1_sum += get_part1_value(line)
        part2_sum += get_part2_value(line)

    print(part1_sum)
    print(part2_sum)
