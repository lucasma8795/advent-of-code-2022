from itertools import product
from copy import deepcopy

def get_max_score(data):
	X_MAX, Y_MAX = len(data[0]), len(data)
	DIR_DOWN, DIR_UP = (0, 1), (0, -1)
	DIR_LEFT, DIR_RIGHT = (-1, 0), (1, 0)

	empty = [[0 for _ in range(X_MAX)] for _ in range(Y_MAX)]
	left, right, down, up = [deepcopy(empty) for _ in range(4)]

	def _search(init_pos, dir, map):
		nums_dist = [None for _ in range(10)]
		x, y = init_pos
		cur_dist = 0
		while True:
			num, blocking_dist = data[y][x], 0
			for i in range(num, 10):
				if nums_dist[i] is None: continue
				blocking_dist = max(blocking_dist, nums_dist[i])

			nums_dist[num] = cur_dist
			map[y][x] = cur_dist - blocking_dist

			x += dir[0]
			y += dir[1]
			if x == -1 or x == X_MAX or y == -1 or y == Y_MAX: break
			cur_dist += 1
	
	for y in range(Y_MAX): # looking from left
		_search((0, y), DIR_RIGHT, left)
	
	for y in range(Y_MAX-1, -1, -1): # looking from right
		_search((X_MAX-1, y), DIR_LEFT, right)
	
	for x in range(X_MAX): # looking from up
		_search((x, 0), DIR_DOWN, up)
	
	for x in range(X_MAX-1, -1, -1): # looking from down
		_search((x, Y_MAX-1), DIR_UP, down)

	out = 0
	for x, y in product(range(X_MAX), range(Y_MAX)):
		cur_score = up[y][x] * down[y][x] * left[y][x] * right[y][x]
		out = max(out, cur_score)
	return out

data = []
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		data.append(list(map(int, line.strip())))

ans = get_max_score(data)
print(ans)