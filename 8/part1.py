def count_visible(data):
	X_MAX, Y_MAX = len(data[0]), len(data)
	def _search(init_pos, dir):
		init_x, init_y = init_pos[0], init_pos[1]
		flag, last = True, data[init_y][init_x]
		visible.append(init_x*1000+init_y)
		x, y = init_pos
		while flag:
			x += dir[0]
			y += dir[1]
			if x == -1 or x == X_MAX or y == -1 or y == Y_MAX: break
			cur = data[y][x]
			if cur > last:
				visible.append(x*1000+y)
			last = max(last, cur)

	visible = []
	DIR_DOWN, DIR_UP = (0, 1), (0, -1)
	DIR_LEFT, DIR_RIGHT = (-1, 0), (1, 0)
	for x in range(X_MAX):
		_search((x, 0), DIR_DOWN)
	for x in range(X_MAX):
		_search((x, Y_MAX-1), DIR_UP)
	for y in range(Y_MAX):
		_search((0, y), DIR_RIGHT)
	for y in range(Y_MAX):
		_search((X_MAX-1, y), DIR_LEFT)

	return len(set(visible))


data = []
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		data.append(list(map(int, line.strip())))

ans = count_visible(data)
print(ans)