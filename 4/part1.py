ans = 0

with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		pair1, pair2 = line.strip().split(",")
		start1, end1 = map(int, pair1.split("-"))
		start2, end2 = map(int, pair2.split("-"))

		if (start2 >= start1 and end2 <= end1) or (start1 >= start2 and end1 <= end2):
			ans += 1

print(ans)