ans = 0

with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		s1, e1, s2, e2 = map(int, line.strip().split(" "))
		
		len1 = e1 - s1 + 1
		len2 = e2 - s2 + 1
		len_total = max(e1, e2) - min(s1, s2) + 1

		if len_total < len1 + len2:
			ans += 1
			print(s1, e1, s2, e2)

print(ans)