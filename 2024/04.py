from common import run_day

xy = complex

DIRECTIONS = [
    xy(1, 0),
    xy(0, 1),
    xy(0, -1),
    xy(-1, 0),
    xy(1, 1),
    xy(1, -1),
    xy(-1, 1),
    xy(-1, -1),
]


def get(M, x, y):
    if not (0 <= x < len(M[0])):
        return None
    if not (0 <= y < len(M)):
        return None
    return M[y][x]


def search(M, x, y, direction, s):
    for c in s:
        if not (0 <= x < len(M[0])):
            return False
        if not (0 <= y < len(M)):
            return False
        if M[int(y)][int(x)] != c:
            return False

        x += direction.real
        y += direction.imag

    return True


def is_x(M, x, y):
    return (
            (
                    get(M, x - 1, y - 1) == 'M' and get(M, x + 1, y + 1) == 'S'
                    or get(M, x - 1, y - 1) == 'S' and get(M, x + 1, y + 1) == 'M'
            )
            and (
                    get(M, x - 1, y + 1) == 'M' and get(M, x + 1, y - 1) == 'S'
                    or get(M, x - 1, y + 1) == 'S' and get(M, x + 1, y - 1) == 'M'
            )
    )


def main(f):
    M = f.read().splitlines()
    first_total = 0
    second_total = 0
    for y in range(len(M)):
        for x in range(len(M[0])):
            for d in DIRECTIONS:
                first_total += search(M, x, y, d, 'XMAS')

            second_total += M[y][x] == 'A' and is_x(M, x, y)

    print(first_total)
    print(second_total)


if __name__ == '__main__':
    run_day(4, main)
