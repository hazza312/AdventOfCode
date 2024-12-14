from common import run_day

xy = complex

DIRECTIONS = [
    xy(1, 0),
    xy(-1, 0),
    xy(0, 1),
    xy(0, -1)
]

def get(M, xy):
    if not ((0 <= xy.imag < len(M)) and (0 <= xy.real < len(M[0]))):
        return None

    return M[int(xy.imag)][int(xy.real)]

def count_peaks(M, start):
    Q = [start]
    visited = set()
    while len(Q):
        curr = Q.pop(0)
        curr_height = get(M, curr)
        visited.add(curr)

        for d in DIRECTIONS:
            next = curr + d
            if (next_height := get(M, next)) is not None \
                    and next_height - curr_height == 1 \
                    and not next in visited:
                Q.append(next)

    return sum(get(M, p) == 9 for p in visited)

def calculate_rating(M, curr):
    if (curr_height := get(M, curr)) == 9:
        return 1

    total = 0
    for d in DIRECTIONS:
        next = curr + d
        if (next_height := get(M, next)) is not None and next_height - curr_height == 1:
            total += calculate_rating(M, next)

    return total

def main(f):
    M = [[None if n == '.' else int(n) for n in line] for line in f.read().splitlines()]
    trail_heads = [xy(x, y) for x in range(len(M[0])) for y in range(len(M)) if M[y][x] == 0]

    print(sum(count_peaks(M, start) for start in trail_heads))
    print(sum(calculate_rating(M, start) for start in trail_heads))

if __name__ == '__main__':
    run_day(10, main)
