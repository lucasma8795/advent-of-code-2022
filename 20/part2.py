data = []
with open("./data.txt", "r") as fo:
	for c, line in enumerate(fo.readlines()):
		num = int(line.strip()) * 811589153
		data.append((c, num))

def find_ix(old_ix):
	for i in range(len(data)):
		if data[i][0] == old_ix:
			return i

for _ in range(10):
	for old_ix in range(len(data)):
		cur_ix = find_ix(old_ix)
		value = data[cur_ix][1]

		new_ix = (cur_ix + value - 1) % (len(data)-1) + 1
		data.pop(cur_ix)
		data.insert(new_ix, (old_ix, value))

# find zero pos
zero_ix = None
for c, p in enumerate(data):
	_, num = p
	if num == 0:
		zero_ix = c
		break

ix_1, ix_2, ix_3 = (zero_ix+1000)%len(data), (zero_ix+2000)%len(data), (zero_ix+3000)%len(data)
ans = data[ix_1][1] + data[ix_2][1] + data[ix_3][1]
print(ans)