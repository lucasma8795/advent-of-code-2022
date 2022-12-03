rounds = []
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		tmp1, tmp2 = line.strip().split(" ")
		map1 = ["A", "B", "C"]
		map2 = ["X", "Y", "Z"]
		rounds.append([map1.index(tmp1), map2.index(tmp2)])

ans = 0
for c1, c2 in rounds:
	m = (c2 - c1 + 3)%3
	if m == 1:
		ans += 6
	elif m == 0:
		ans += 3
	ans += c2 + 1

print(ans)