from itertools import chain

data = []
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		data.append(line.strip())
	
ans = 0
for i in range(100):
	char_count = [0 for _ in range(127)]
	s1, s2, s3 = set(data[i*3]), set(data[i*3+1]), set(data[i*3+2])

	for char in chain(s1, s2, s3):
		char_count[ord(char)] += 1

	tmpans = char_count.index(3)
	if 65 <= tmpans <= 90:
		tmpans -= 65
		tmpans += 27
	else:
		tmpans -= 97
		tmpans += 1
	ans += tmpans

print(ans)