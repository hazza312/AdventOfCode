from sys import stdin
import re 

NUM_STACKS = 9
MOVE_REGEX = re.compile(r"move (\d+) from (\d+) to (\d+)")


def read_stack_line(line):
    return [(i, line[i*4+1]) for i in range(NUM_STACKS) 
                if i < len(line) and line[i*4+1] != ' ']

def read_stacks(lines):
    stacks = [[] for _ in range(NUM_STACKS)]

    for lineno, line in enumerate(lines):
        if line.startswith(" 1"):
            break 

        for i, next_top in read_stack_line(line):
            stacks[i].insert(0, next_top)

    return stacks, lines[lineno+2:]

def cratemover_9000(stacks, n, src, dst):
    stacks[dst] += stacks[src][:-n-1:-1]
    stacks[src] = stacks[src][:-n]

def cratemover_9001(stacks, n, src, dst):
    stacks[dst] += stacks[src][-n:]
    stacks[src] = stacks[src][:-n]    

def do_moves(stacks, moves, mover):
    for move in moves:
        n, src, dst = map(int, MOVE_REGEX.match(move).groups())
        mover(stacks, n, src-1, dst-1)

    return ''.join(s[-1] for s in stacks if len(s) > 0)


lines = stdin.readlines()
print(do_moves(*read_stacks(lines), cratemover_9000))
print(do_moves(*read_stacks(lines), cratemover_9001))
