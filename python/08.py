from sys import stdin
from functools import reduce
from operator import mul

def all_coords(grid):
    return [(x, y) for y in range(len(grid)    ) for x in range(len(grid[0]))]

def rays(grid, x, y):
    """
    Return rays (iterator of coordinates) in each cardinal direction.
    Starting from first coordinate after (x, y) towards the grid edge.
    """

    return [
        ((x, i) for i in range(y-1, -1, -1)),      # towards top edge
        ((x, i) for i in range(y+1, len(grid))),   # bottom
        ((i, y) for i in range(x-1, -1, -1)),      # left
        ((i, y) for i in range(x+1, len(grid[0]))) # right
    ]


def direction_unblocked(grid, x, y, ray):
    return all(grid[yi][xi] < grid[y][x] for xi, yi in ray)

def is_visible(grid, c):
    return any(direction_unblocked(grid, *c, r) for r in rays(grid, *c))

def num_visible_trees(grid):
    return sum(is_visible(grid, c) for c in all_coords(grid))


def scenic_in_direction(grid, x, y, ray):
    count = 0
    for xi, yi in ray:
        count += 1

        if grid[yi][xi] >= grid[y][x]:
            break

    return count

def scenic_score(grid, c):
    direction_scores = (scenic_in_direction(grid, *c, r) for r in rays(grid, *c))
    return reduce(mul, direction_scores, 1)

def max_scenic_score(grid):
    return max(scenic_score(grid, c) for c in all_coords(grid))


grid = [[int(c) for c in line.strip()] for line in stdin]
print(num_visible_trees(grid))
print(max_scenic_score(grid))
