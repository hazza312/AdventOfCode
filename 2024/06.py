from common import run_day

xy = complex

def in_range(M, xy):
    return 0 <= xy.real < len(M[0]) and 0 <= xy.imag < len(M)

def get(M, xy):
    if not in_range(M, xy):
        return None
    return M[int(xy.imag)][int(xy.real)]

def part1(M, curr, d=xy(0, -1)):
    visited = set()
    while in_range(M, curr):
        visited.add(curr)
        if get(M, curr + d) == '#':
            d *= xy(0, 1)
        else:
            curr += d

    return len(visited)


def has_loop(M, curr, d):
    visited = set()
    while in_range(M, curr):
        visited.add((curr, d))
        next = curr + d
        if (next, d) in visited:
            return True
        if get(M, next) == '#':
            d *= xy(0, 1)
        else:
            curr = next

    return False


def part2(M, curr, d=xy(0, -1)):
    possible_obstructions = 0
    for y in range(len(M)):
        M[y] = list(M[y])
        for x in range(len(M[0])):
            if M[y][x] != '#':
                M[y][x] = '#'
                possible_obstructions += has_loop(M, curr, d)
                M[y][x] = '.'

    return possible_obstructions

def main(f):
    M = f.read().splitlines()
    curr = xy(*[(M[y].find('^'), y) for y in range(len(M)) if '^' in M[y]][0])

    print(part1(M, curr))
    print(part2(M, curr))

if __name__ == '__main__':
    run_day(6, main)
