def unique(data):
	return len(data) == len(set(data))

with open("./data.txt", "r") as fo:
	data = fo.read().strip()

window = 14
for i in range(len(data)-window):
	if unique(data[i:i+window]):
		print(i+window)
		exit()