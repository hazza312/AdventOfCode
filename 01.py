from sys import stdin

elves = [map(int, elf.split()) for elf in stdin.read().split('\n\n')]
elf_sums = sorted(map(sum, elves))

print(elf_sums[-1])
print(sum(elf_sums[-3:]))
