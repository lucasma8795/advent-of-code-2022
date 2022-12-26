import numpy as np

LIMIT = 25

def solve(data):
	xy = np.zeros(shape=(LIMIT, LIMIT, LIMIT))
	xz = np.zeros(shape=(LIMIT, LIMIT, LIMIT))
	yz = np.zeros(shape=(LIMIT, LIMIT, LIMIT))

	for x, y, z in data:
		xy[x][y][z] += 1
		xy[x][y][z+1] += 1

		xz[x][y][z] += 1
		xz[x][y+1][z] += 1

		yz[x][y][z] += 1
		yz[x+1][y][z] += 1

	return np.count_nonzero(xy == 1) + np.count_nonzero(xz == 1) + np.count_nonzero(yz == 1)

data = []
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		data.append(map(int, line.strip().split(",")))
ans = solve(data)
print(ans)