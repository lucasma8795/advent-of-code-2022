Y = 2000000

segments = []
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		s_x, s_y, b_x, b_y = map(int, line.strip().split(' '))
		d_x, d_y = abs(s_x - b_x), abs(s_y - b_y)
		d = d_x + d_y
		if abs(s_y - Y) > d: continue

		start = s_x - d + abs(s_y - Y)
		end = s_x + d - abs(s_y - Y)
		segments.append((start, False))
		segments.append((end, True))

segments.sort(key=lambda x: x[0])

# klee's algorithm
counter, ans = 0, 0
cur, prev = segments[0], None

for i in range(len(segments)):
	cur = segments[i]
	if i > 0:
		if cur[0] > prev[0] and counter > 0:
			ans += cur[0] - prev[0]

	if cur[1]: counter -= 1
	else: counter += 1
	prev = cur

print(ans)