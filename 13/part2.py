from json import loads

data = []
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		data.append(loads(line))

s2, s6 = 1, 2 # indices of dividers

def get_first(item):
	if isinstance(item, int):
		return item
	else:
		if len(item) == 0: return -1
		return get_first(item[0])

for item in data:
	num = get_first(item)
	if num < 2: s2 += 1
	if num < 6: s6 += 1

print(s2*s6)