with open("./data.txt", "r") as fo:
	lines = [line.strip() for line in fo.readlines()]

data = []
cur = 0

for line in lines:
	if line == "":
		data.append(cur)
		cur = 0
	else:
		cur += int(line)

data.sort()
print(sum(data[:-3]))