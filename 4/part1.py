ans = 0

with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		s1, e1, s2, e2 = map(int, line.strip().split(" "))

		if s1 <= s2 <= e2 <= e1 or s2 <= s1 <= e1 <= e2:
			ans += 1

print(ans)