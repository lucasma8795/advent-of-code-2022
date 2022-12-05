data = [[] for _ in range(10)]
with open("./crate.txt", "r") as fo:
	for line in fo.readlines():
		for i in range(1, 10):
			char = line[i*2-2]
			if char == " ": continue
			data[i].insert(0, char)

instructions = []
with open("./instructions.txt", "r") as fo:
	for line in fo.readlines():
		instructions.append(map(int, line.strip().split(" ")))

for count, prev, new in instructions:
	loc = len(data[new])
	for i in range(count):
		char = data[prev].pop()
		data[new].insert(loc, char)

print("".join([stack[-1] for stack in data[1:]]))