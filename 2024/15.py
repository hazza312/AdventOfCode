from itertools import product

from common import run_day

xy = complex

DIRECTIONS = {
    '^': xy(0, -1),
    'v': xy(0, 1),
    '<': xy(-1, 0),
    '>': xy(1, 0)
}
HORIZONTAL = (DIRECTIONS['<'], DIRECTIONS['>'])
VERTICAL = (DIRECTIONS['^'], DIRECTIONS['v'])

def get(M, xy):
    return M[int(xy.imag)][int(xy.real)]

def setm(M, dst, val):
    M[int(dst.imag)][int(dst.real)] = val

def merge_if_all_nonempty(*ls):
    return [] if any(len(l) == 0 for l in ls) else list(set([x for l in ls for x in l]))

def to_move(M, src, dir):
    """All points needed to move in direction dir so that src can move, or empty list if not possible"""
    dst = src + dir
    if (c := get(M, dst)) == '#':       # src can't move to dst
        return []
    if c == '.':                        # src can move without shifting anything else
        return [src]

    # src can only move when all related box points can also be moved
    if c == 'O' or (dir in HORIZONTAL and c in '[]'):
        return merge_if_all_nonempty([src], to_move(M, dst, dir))
    if dir in VERTICAL:
        if c == '[':
            return merge_if_all_nonempty([src], to_move(M, dst, dir), to_move(M, dst + xy(1, 0), dir))
        if c == ']':
            return merge_if_all_nonempty([src], to_move(M, dst, dir), to_move(M, dst + xy(-1, 0), dir))

    return []

def move(M, src, dir):
    if len(points := to_move(M, src, dir)) > 0:
        # order by opposite direction
        points.sort(key=lambda p: (p.real * -dir.real, p.imag * -dir.imag))
        for p in points:
            setm(M, p+dir, get(M, p))
            setm(M, p,'.')

        return src + dir

    return src

def get_sum(M):
    return sum(y * 100 + x for x, y in product(range(len(M[0])), range(len(M))) if M[y][x] in 'O[')

def get_start(mm):
    return min(xy(l.index('@'), y) for y, l in enumerate(mm) if '@' in l)

def main(f):
    M1, M2 = [], []
    while line := f.readline().strip():
        M1.append(list(line))
        M2.append(list(line.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')))

    curr1, curr2 = get_start(M1), get_start(M2)
    for dir in (c for c in f.read() if c != '\n'):
        curr1 = move(M1, curr1, DIRECTIONS[dir])
        curr2 = move(M2, curr2, DIRECTIONS[dir])

    print(get_sum(M1))
    print(get_sum(M2))


if __name__ == '__main__':
    run_day(15, main, 'c')
