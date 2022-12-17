from dataclasses import dataclass, field
from itertools import product
from sys import maxsize as INF
from typing import Optional, Self

@dataclass
class Pair:
	x: int
	y: int
	def __add__(self, other): return Pair(self.x+other.x, self.y+other.y)
	def out_of_bounds(self):
		return self.x < 0 or self.x >= ncols or self.y < 0 or self.y >= nrows

@dataclass
class Node:
	height: int = 0
	cost: int = INF
	prev: Optional[Self] = None
	seen: bool = False
	neighbours: list = field(default_factory=list)
	def __lt__(self, other): return self.cost < other.cost

DIR_UP, DIR_DOWN = Pair(-1, 0), Pair(1, 0)
DIR_LEFT, DIR_RIGHT = Pair(0, -1), Pair(0, 1)
DIRS = [DIR_UP, DIR_DOWN, DIR_LEFT, DIR_RIGHT]

def build_vertices(data):
	verts = [Node() for _ in range(nrows*ncols)]
	for r, c in product(range(nrows), range(ncols)):
		verts[r*ncols+c].height = data[r][c]

	for r, c in product(range(nrows), range(ncols)):
		u = verts[r*ncols+c]
		u_pos = Pair(c, r)

		for dir in DIRS:
			v_pos = u_pos + dir
			if v_pos.out_of_bounds(): continue
			v = verts[v_pos.y*ncols+v_pos.x]
			if v.height - u.height > 1: continue
			u.neighbours.append(v)

	return verts

data = []
start, end = None, None
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		data.append(list(map(ord, line.strip())))
nrows, ncols = len(data), len(data[0])

for r, c in product(range(nrows), range(ncols)):
	if data[r][c] == ord('S'):
		data[r][c] = ord('a')
		start = r*ncols+c

	elif data[r][c] == ord('E'):
		data[r][c] = ord('z')
		end = r*ncols+c

verts = build_vertices(data)

def dijkstra(verts, start, end):
	q = []
	verts[start].cost = 0
	for v in verts: q.append(v)
	
	while len(q) > 0:
		u = q.pop(min(range(len(q)), key=q.__getitem__))
		u.seen = True
		for v in u.neighbours:
			if v.seen: continue
			alt = u.cost + 1
			if alt < v.cost:
				v.cost = alt
				v.prev = u

		if verts[end].prev is not None:
			return verts[end].cost

ans = dijkstra(verts, start, end)
print(ans)