rounds = []
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		tmp1, tmp2 = line.strip().split(" ")
		map1 = ["A", "B", "C"]
		map2 = ["X", "Y", "Z"]
		rounds.append([map1.index(tmp1), map2.index(tmp2)])

ans = 0
for opp, me in rounds:
	score = (me - opp + 3)%3
	if score == 1:
		ans += 6
	elif score == 0:
		ans += 3
	ans += me + 1

print(ans)