from sys import stdin

xy = complex

FALL_DIRECTIONS = (xy(0, 1), xy(-1, 1), xy(1, 1))
SAND_SOURCE = xy(500, 0)
SAND, ROCK = '.#'


def signum(x):
    return 0 if x == 0 else abs(x) // x 

def direction(diff):
    return xy(signum(diff.real), signum(diff.imag))

def read_grid(lines):
    grid = {}

    for line in lines:
        coords = [xy(*map(int, s.split(','))) for s in line.split(' -> ')]
        for c1, c2 in zip(coords, coords[1:]):
            dxy = direction(c2 - c1)
            while c1 != c2 + dxy:
                grid[c1] = ROCK 
                c1 += dxy

    return grid

def abyss_start(grid):
    return max(grid.keys(), key=lambda c: c.imag).imag


def drop_grain(grid, abyss_start):
    """
    Drop a grain of sand from source.
    Return True if grain fell into abyss (& also place)
    """

    sand = SAND_SOURCE
    while sand.imag <= abyss_start:
        for d in FALL_DIRECTIONS:
            if sand + d not in grid:
                sand += d
                break 
        else:
            break

    grid[sand] = SAND
    return sand.imag <= abyss_start


def grains_dropped_before_abyss(grid, abyss_start):
    num_grains = 0
    while drop_grain(grid, abyss):
        num_grains += 1

    return num_grains


def grains_dropped_before_block_source(grid, abyss_start):
    num_grains = 0
    while SAND_SOURCE not in grid:
        drop_grain(grid, abyss)
        num_grains += 1

    return num_grains


grid = read_grid(stdin) 
grid2 = dict(grid)
abyss = abyss_start(grid)

print(grains_dropped_before_abyss(grid, abyss_start))
print(grains_dropped_before_block_source(grid2, abyss_start))
