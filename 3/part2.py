from itertools import chain

data = []
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		data.append(line.strip())
	
ans = 0
for i in range(len(data)//3):
	str1, str2, str3 = set(data[i*3]), set(data[i*3+1]), set(data[i*3+2])
	char = (str1 & str2 & str3).pop()

	priority = ord(char)
	if 65 <= priority <= 90:
		priority += (-65 + 27)
	else:
		priority += (-97 + 1)
	ans += priority

print(ans)