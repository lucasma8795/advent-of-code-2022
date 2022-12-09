def count_visible(data):
	visible = []
	X_MAX, Y_MAX = len(data[0]), len(data)
	DIR_DOWN, DIR_UP = (0, 1), (0, -1)
	DIR_LEFT, DIR_RIGHT = (-1, 0), (1, 0)

	def _search(init_pos, dir):
		x, y = init_pos
		last = data[y][x]
		visible.append(x*1000+y)
		while True:
			x += dir[0]
			y += dir[1]
			if x == -1 or x == X_MAX or y == -1 or y == Y_MAX: break
			cur = data[y][x]
			if cur > last: visible.append(x*1000+y)
			last = max(last, cur)

	for y in range(Y_MAX): # looking from left
		_search((0, y), DIR_RIGHT)

	for y in range(Y_MAX): # looking from right
		_search((X_MAX-1, y), DIR_LEFT)
	
	for x in range(X_MAX): # looking from up
		_search((x, 0), DIR_DOWN)

	for x in range(X_MAX): # looking from down
		_search((x, Y_MAX-1), DIR_UP)

	return len(set(visible)) # unique visible trees

data = []
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		data.append(list(map(int, line.strip())))

ans = count_visible(data)
print(ans)