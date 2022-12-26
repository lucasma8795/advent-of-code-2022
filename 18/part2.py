import numpy as np
from collections import deque
from itertools import product

LIMIT = 25

def out_of_bounds(x, y, z):
	return not (0 <= x < LIMIT) or not (0 <= y < LIMIT) or not (0 <= z < LIMIT)

def flood_fill(data, start=(0,0,0)):
	visited = set([start])
	q = deque([start])
	while q:
		node = q.pop()
		x, y, z = node
		for dx, dy, dz in zip((-1,1,0,0,0,0), (0,0,-1,1,0,0), (0,0,0,0,-1,1)):
			new_node = (x+dx, y+dy, z+dz)
			if out_of_bounds(*new_node): continue
			if new_node in visited or new_node in data: continue
			visited.add(new_node)
			q.append(new_node)
	return visited

def solve(data):
	xy = np.zeros(shape=(LIMIT+1, LIMIT+1, LIMIT+1))
	xz = np.zeros(shape=(LIMIT+1, LIMIT+1, LIMIT+1))
	yz = np.zeros(shape=(LIMIT+1, LIMIT+1, LIMIT+1))

	for x, y, z in data:
		xy[x][y][z] += 1
		xy[x][y][z+1] += 1

		xz[x][y][z] += 1
		xz[x][y+1][z] += 1

		yz[x][y][z] += 1
		yz[x+1][y][z] += 1

	return np.count_nonzero(xy == 1) + np.count_nonzero(xz == 1) + np.count_nonzero(yz == 1)

data = set()
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		data.add(tuple(map(int, line.strip().split(","))))

all = set()
for x, y, z in product(range(LIMIT), repeat=3):
	all.add((x, y, z))

ext = flood_fill(data)
solid = all - ext
ans = solve(solid)
print(ans)