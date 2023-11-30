from sys import stdin
from json import loads
from functools import cmp_to_key

DIVIDERS = [[[2]], [[6]]]

def is_singleton(l):
    return type(l) == list and len(l) == 1 and type(l[0]) == int

def in_order(a, b):
    if is_singleton(a) and is_singleton(b):
        return a[0] - b[0]
    
    if type(a) != list:
        return in_order([a], b)
    
    if type(b) != list:
        return in_order(a, [b])
    
    for ai, bi in zip(a, b):
        if (cmp := in_order(ai, bi)) != 0:
            return cmp 
    
    return len(a) - len(b)


lists = [loads(s) for group in stdin.read().split('\n\n') for s in group.splitlines()]
pairs = [lists[i:i+2] for i in range(0, len(lists), 2)]

results = [in_order(a, b) for a, b in pairs]
in_order_index_sum = sum(i+1 for i, result in enumerate(results) if result < 0)
print(in_order_index_sum)

sorted_items = sorted(lists + DIVIDERS, key=cmp_to_key(in_order))
signal = (sorted_items.index(DIVIDERS[0]) + 1) * (sorted_items.index(DIVIDERS[1]) + 1)
print(signal)