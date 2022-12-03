from itertools import chain

data = []
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		data.append(line.strip())

ans = 0
for string in data:
	char_count = [0 for _ in range(127)]
	mid_pos = len(string)//2
	left, right = set(string[:mid_pos]), set(string[mid_pos:])

	for char in chain(left, right):
		char_count[ord(char)] += 1

	tmpans = char_count.index(2)
	if 65 <= tmpans <= 90:
		tmpans -= 65
		tmpans += 27
	else:
		tmpans -= 97
		tmpans += 1
	ans += tmpans

print(ans)
