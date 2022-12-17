from heapq import *
from sys import maxsize as INF
from dataclasses import dataclass

@dataclass
class Pair:
	x: int
	y: int
	def __add__(self, other): return Pair(self.x+other.x, self.y+other.y)
	def out_of_bounds(self):
		return self.x < 0 or self.x >= ncols or self.y < 0 or self.y >= nrows
	def __hash__(self):
		return self.y*ncols+self.x

DIR_UP, DIR_DOWN = Pair(-1, 0), Pair(1, 0)
DIR_LEFT, DIR_RIGHT = Pair(0, -1), Pair(0, 1)
DIRS = [DIR_UP, DIR_DOWN, DIR_LEFT, DIR_RIGHT]

data = []
start, end = None, None
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		data.append(list(map(ord, line.strip())))
nrows, ncols = len(data), len(data[0])
ntotal = nrows*ncols

for r in range(nrows):
	for c in range(ncols):
		if data[r][c] == ord('S'):
			data[r][c] = ord('a')
			start = r*ncols+c
		elif data[r][c] == ord('E'):
			data[r][c] = ord('z')
			end = r*ncols+c

def build_graph(data):
	G = [[] for _ in range(ntotal)]
	for r in range(nrows):
		for c in range(ncols):
			u = data[r][c]
			u_pos = Pair(c, r)

			for dir in DIRS:
				v_pos = u_pos + dir
				if v_pos.out_of_bounds(): continue
				v = data[v_pos.y][v_pos.x]
				if v - u > 1: continue
				G[hash(u_pos)].append(hash(v_pos))

	return G

def dijkstra(G, start):
	dist = [INF for _ in range(ntotal)]
	prev = [None for _ in range(ntotal)]
	seen = [False for _ in range(ntotal)]
	dist[start] = 0

	Q = []
	for i in range(ntotal):
		Q.append((dist[i], i))
	heapify(Q)

	while len(Q):
		_, u = heappop(Q)
		if seen[u]: continue
		seen[u] = True
		for v in G[u]:
			alt = dist[u] + 1
			if alt < dist[v]:
				dist[v], prev[v] = alt, u
				heappush(Q, (alt, v))
	return dist

G = build_graph(data)
dist = dijkstra(G, start)
ans = dist[end]
print(ans)