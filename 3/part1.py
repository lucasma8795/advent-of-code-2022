data = []
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		data.append(line.strip())

ans = 0
for string in data:
	mid_pos = len(string)//2
	left, right = set(string[:mid_pos]), set(string[mid_pos:])
	char = (left & right).pop()

	priority = ord(char)
	if 65 <= priority <= 90:
		priority += (-65 + 27)
	else:
		priority += (-97 + 1)
	ans += priority

print(ans)
