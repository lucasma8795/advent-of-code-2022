from itertools import product
from copy import deepcopy

def get_max_score(data):
	X_MAX, Y_MAX = len(data[0]), len(data)
	zero_grid = [[0 for _ in range(X_MAX)] for _ in range(Y_MAX)]
	left, right, down, up = [deepcopy(zero_grid) for _ in range(4)]

	for y in range(Y_MAX):
		num_dist = [-1 for _ in range(10)]
		for x in range(X_MAX):
			cur_num, cur_dist, blocking = data[y][x], x, 0
			for j in range(cur_num, 10):
				if num_dist[j] == -1: continue
				blocking = max(blocking, num_dist[j])
			num_dist[cur_num] = cur_dist
			left[y][x] = cur_dist - blocking

	for y in range(Y_MAX):
		num_dist = [-1 for _ in range(10)]
		for x in range(X_MAX-1, -1, -1):
			cur_num, cur_dist, blocking = data[y][x], X_MAX-x-1, 0
			for j in range(cur_num, 10):
				if num_dist[j] == -1: continue
				blocking = max(blocking, num_dist[j])
			num_dist[cur_num] = cur_dist
			right[y][x] = cur_dist - blocking

	for x in range(X_MAX):
		num_dist = [-1 for _ in range(10)]
		for y in range(Y_MAX):
			cur_num, cur_dist, blocking = data[y][x], y, 0
			for j in range(cur_num, 10):
				if num_dist[j] == -1: continue
				blocking = max(blocking, num_dist[j])
			num_dist[cur_num] = cur_dist
			down[y][x] = cur_dist - blocking

	for x in range(X_MAX):
		num_dist = [-1 for _ in range(10)]
		for y in range(Y_MAX-1, -1, -1):
			cur_num, cur_dist, blocking = data[y][x], Y_MAX-y-1, 0
			for j in range(cur_num, 10):
				if num_dist[j] == -1: continue
				blocking = max(blocking, num_dist[j])
			num_dist[cur_num] = cur_dist
			up[y][x] = cur_dist - blocking
	
	out = 0
	for x, y in product(range(X_MAX), range(Y_MAX)):
		out = max(out, up[y][x] * down[y][x] * left[y][x] * right[y][x])
	return out


data = []
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		data.append(list(map(int, line.strip())))

ans = get_max_score(data)
print(ans)