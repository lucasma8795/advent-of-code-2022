data = [[] for _ in range(10)]
with open("./crate.txt", "r") as fo:
	for line in fo.readlines():
		for i in range(1, 10):
			char = line[i*2-2]
			if char == " ": continue
			data[i].insert(0, char)

with open("./instructions.txt", "r") as fo:
	for line in fo.readlines():
		count, prev, new = map(int, line.strip().split(" "))
		for i in range(count):
			char = data[prev].pop()
			data[new].append(char)

print("".join([stack[-1] for stack in data[1:]]))