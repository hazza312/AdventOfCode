from sys import stdin

# Slight hack treating the real and imaginary parts of a complex number as
# x, y components of a vector/coordinate.

xy = complex

OFFSETS = {'R': xy(1, 0), 'L': xy(-1, 0), 'U': xy(0, 1), 'D': xy(0, -1)}
MOVE_THRESHOLD = abs(xy(1, 1))

def signum(x):
    return 0 if x == 0 else x / abs(x)

def offset_signum(a, b):
    x1, y1 = a.real, a.imag
    x2, y2 = b.real, b.imag
    return xy(signum(x2 - x1), signum(y2 - y1))

def next_offset(tail, head):
    if abs(head - tail) <= MOVE_THRESHOLD:
        return xy(0, 0)
    
    return offset_signum(tail, head)
    
def num_tail_positions(commands, rope_length):
    rope = [xy(0, 0)] * rope_length
    tail_visited = {rope[-1]}
    
    for direction, n in commands:
        for _ in range(int(n)):
            rope[0] += OFFSETS[direction]
            for i in range(1, len(rope)):
                rope[i] += next_offset(rope[i], rope[i-1])

            tail_visited.add(rope[-1])
                
    return len(tail_visited)        


commands = [line.split() for line in stdin.readlines()]
print(num_tail_positions(commands, 2)) 
print(num_tail_positions(commands, 10)) 
