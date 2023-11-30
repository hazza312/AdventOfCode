from sys import stdin

# Slight hack treating the real and imaginary parts of a complex number as
# x, y components of a vector/coordinate.

xy = complex

OFFSETS = {'R': xy(1, 0), 'L': xy(-1, 0), 'U': xy(0, 1), 'D': xy(0, -1)}
MOVE_THRESHOLD = abs(xy(1, 1))

def signum(x):
    return 0 if x == 0 else x / abs(x)

def next_offset(offset):
    if abs(offset) <= MOVE_THRESHOLD:
        return xy(0, 0)
    
    return xy(signum(offset.real), signum(offset.imag))
    
def num_tail_positions(commands, rope_length):
    rope = [xy(0, 0)] * rope_length
    tail_visited = {rope[-1]}
    
    for direction, n in commands:
        for _ in range(int(n)):
            rope[0] += OFFSETS[direction]
            for i in range(1, len(rope)):
                rope[i] += next_offset(rope[i-1] - rope[i])

            tail_visited.add(rope[-1])
                
    return len(tail_visited)        


commands = [line.split() for line in stdin.readlines()]
print(num_tail_positions(commands, 2)) 
print(num_tail_positions(commands, 10)) 
