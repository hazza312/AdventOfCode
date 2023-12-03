import re
from sys import stdin

xy = complex

digit_to_number_id = {}  # maps xy of digit in grid to index in numbers list below
numbers = []
symbols = {}


def neighbours(cell: xy):
    return [
        cell + xy(dx, dy)
        for dx in range(-1, 2)
        for dy in range(-1, 2)
        if abs(xy(dx, dy))
    ]


def part_sum():
    cells_neighbouring_symbols = {n for s in symbols for n in neighbours(s)}
    digit_cells = digit_to_number_id.keys()
    digit_cells_neighbouring_symbols = cells_neighbouring_symbols & digit_cells

    number_ids = {digit_to_number_id[i] for i in digit_cells_neighbouring_symbols}
    return sum(numbers[i] for i in number_ids)


def gear_ratio_sum():
    gear_cells = [s for s in symbols if symbols[s] == '*']
    sum = 0
    for gear in gear_cells:
        number_ids = {digit_to_number_id.get(n) for n in neighbours(gear)} - {None}
        if len(number_ids) == 2:
            a, b = number_ids
            sum += numbers[a] * numbers[b]

    return sum


def read_input():
    for y, line in enumerate(stdin):
        for num in re.finditer(r'\d+', line):
            numbers.append(int(num.group()))
            for x in range(num.start(), num.end()):
                digit_to_number_id[xy(x, y)] = len(numbers) - 1

        for symbol in re.finditer(r'[^\d\s.]', line):
            symbols[xy(symbol.start(), y)] = symbol.group()


if __name__ == '__main__':
    read_input()
    print(part_sum())
    print(gear_ratio_sum())
