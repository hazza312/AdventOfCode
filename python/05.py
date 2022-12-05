from sys import stdin
import re 

NUM_STACKS = 9
MOVE_REGEX = re.compile(r"move (\d+) from (\d+) to (\d+)")


def read_stack_line(line):
	return [line[i] for i in range(1, NUM_STACKS * 4, 4) if i < len(line)]

def read_stacks(lines):
	stacks = [[] for _ in range(NUM_STACKS)]

	for lineno, line in enumerate(lines):
		stack_line = read_stack_line(line)
		if stack_line[0].isdigit():
			break
		
		for i, top_of_stack in enumerate(stack_line):
			if top_of_stack != ' ':
				stacks[i].insert(0, top_of_stack)

	return stacks, lines[lineno+2:]

def cratemover_9000(stacks, n, src, dst):
	stacks[dst - 1] += stacks[src - 1][:-n-1:-1]
	stacks[src - 1] = stacks[src - 1][:-n]

def cratemover_9001(stacks, n, src, dst):
	stacks[dst - 1] += stacks[src - 1][-n:]
	stacks[src - 1] = stacks[src - 1][:-n]	

def do_moves(stacks, moves, mover):
	for move in moves:
		mover(stacks, *map(int, MOVE_REGEX.match(move).groups()))

	return ''.join(s[-1] for s in stacks if len(s) > 0)


lines = stdin.readlines()
print(do_moves(*read_stacks(lines), cratemover_9000))
print(do_moves(*read_stacks(lines), cratemover_9001))
