rounds = []
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		tmp1, tmp2 = line.strip().split(" ")
		map1 = ["A", "B", "C"]
		map2 = ["X", "Y", "Z"]
		rounds.append([map1.index(tmp1), map2.index(tmp2)])

ans = 0
for opp, res in rounds:
	ans += res * 3

	if res == 0: # lose
		me = (opp + 2) % 3
	elif res == 1: # draw
		me = opp
	elif res == 2: # win
		me = (opp + 1) % 3
	ans += me + 1
	
print(ans)