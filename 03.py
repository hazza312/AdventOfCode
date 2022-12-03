from sys import stdin
from functools import reduce

GROUP_SIZE = 3

def priority(c):
    if 'a' <= c <= 'z':
        return ord(c) - ord('a') + 1
    
    return ord(c) - ord('A') + 27
    
def groups_priority(groups):
    reducer = lambda acc, group: set(acc) & set(group)
    return priority(reduce(reducer, groups).pop())

def rucksack_priority(line):
    size = len(line) // 2
    return groups_priority((line[:size], line[size:]))


lines = stdin.read().splitlines()
groups = [lines[i:i+GROUP_SIZE] for i in range(0, len(lines), GROUP_SIZE)]

print(sum(map(rucksack_priority, lines)))
print(sum(map(groups_priority, groups)))