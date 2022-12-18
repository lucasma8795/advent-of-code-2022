# MIN_X, MIN_Y = 0, 0
# MAX_X, MAX_Y = 4000000, 4000000

# def segment_union(segments):
# 	# klee's algorithm
# 	segments.sort(key=lambda x: x[0])
# 	counter, ans = 0, 0
# 	cur, prev = segments[0], None

# 	for i in range(len(segments)):
# 		cur = segments[i]
# 		if i > 0:
# 			if cur[0] > prev[0] and counter > 0:
# 				ans += cur[0] - prev[0]

# 		if cur[1]: counter -= 1
# 		else: counter += 1
# 		prev = cur

# 	return ans


# data = []
# with open("./data.txt", "r") as fo:
# 	for line in fo.readlines():
# 		data.append(list(map(int, line.strip().split(' '))))

# Y = 3042458
# segments = []

# for s_x, s_y, b_x, b_y in data:
# 	d_x, d_y = abs(s_x - b_x), abs(s_y - b_y)
# 	d = d_x + d_y

# 	if abs(s_y - Y) > d: continue
	
# 	start = s_x - d + abs(s_y - Y)
# 	end = s_x + d - abs(s_y - Y)

# 	start = max(start, MIN_X)
# 	end = min(end, MAX_X)

# 	segments.append((start, False))
# 	segments.append((end, True))

# segments.sort(key=lambda x: x[0])
# print(segments)
# total_len = segment_union(segments)
# print(total_len)

# print(3012821*4000000+3042458)