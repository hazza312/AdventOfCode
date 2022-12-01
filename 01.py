from sys import stdin

elves = [map(int, elf.split()) for elf in stdin.read().split('\n\n')]
elf_sums = list(map(sum, elves))

print(max(elf_sums))
print(sum(sorted(elf_sums, reverse=True)[:3]))
