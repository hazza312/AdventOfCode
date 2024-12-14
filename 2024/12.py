from collections import defaultdict
from itertools import pairwise

from shapely import MultiPolygon, box, LineString, union_all
from shapely.ops import linemerge

from common import run_day


def total_price(p, len_fn=lambda p: p.length):
    if isinstance(p, MultiPolygon):
        return sum(total_price(sp, len_fn=len_fn) for sp in p.geoms)

    perimeter = len_fn(p.exterior) + sum(len_fn(i) for i in p.interiors)
    return int(perimeter * p.area)

def sides(l):
    segs = list(pairwise(l.coords))
    hs = linemerge([(x1, y1), (x2, y2)] for (x1, y1), (x2, y2) in segs if y1 == y2)
    vs = linemerge([(x1, y1), (x2, y2)] for (x1, y1), (x2, y2) in segs if x1 == x2)
    return len(hs.geoms) + len(vs.geoms)


def main(f):
    regions = defaultdict(list)
    for y, line in enumerate(f.read().splitlines()):
        for x, val in enumerate(line):
            regions[val].append(box(x, y, x+1, y+1))

    for v in regions:
        regions[v] = union_all(regions[v])

    print(sum(total_price(r) for r in regions.values()))
    print(sum(total_price(r, len_fn=sides) for r in regions.values()))


if __name__ == '__main__':
    run_day(12, main)
