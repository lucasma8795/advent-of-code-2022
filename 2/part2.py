rounds = []
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		tmp1, tmp2 = line.strip().split(" ")
		map1 = ["A", "B", "C"]
		map2 = ["X", "Y", "Z"]
		rounds.append([map1.index(tmp1), map2.index(tmp2)])

ans = 0
for c1, c2 in rounds:
	ans += c2 * 3

	if c2 == 0: # lose
		c3 = (c1 + 2) % 3
	elif c2 == 1: # draw
		c3 = c1
	elif c2 == 2: # win
		c3 = (c1 + 1) % 3
	ans += c3 + 1
	
print(ans)