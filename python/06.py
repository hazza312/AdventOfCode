def find_marker(n, string):
	for i in range(n, len(string)):
		if len(set(string[i-n:i])) == n:
			return i

line = input()
print(find_marker(4, line))
print(find_marker(14, line))
 