from math import ceil, floor

import numpy as np


def get_num_ways(t, d):
    lo, hi = sorted(np.roots([-1, t, -d]))
    return ceil(hi) - floor(lo) - 1


if __name__ == '__main__':
    product = 1
    for t, d in [(46, 208), (85, 1412), (75, 1257), (82, 1410)]:
        product *= get_num_ways(t, d)

    print(product)
    print(get_num_ways(46857582, 208141212571410))