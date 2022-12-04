ans = 0

with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		pair1, pair2 = line.strip().split(",")
		start1, end1 = map(int, pair1.split("-"))
		start2, end2 = map(int, pair2.split("-"))
		
		len_pair1 = end1 - start1 + 1
		len_pair2 = end2 - start2 + 1
		len_total = max(end2 - start1 + 1, end1 - start2 + 1)

		if len_total < (len_pair1 + len_pair2):
			ans += 1

print(ans)