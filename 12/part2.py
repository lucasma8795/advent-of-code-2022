import heapq
import itertools
from sys import maxsize as INF
from copy import deepcopy
from dataclasses import dataclass

class Pos:
	def __init__(self, row, col):
		self.row = row
		self.col = col
	
	def __add__(self, other):
		return Pos(self.row + other.row, self.col + other.col)
	
	def __sub__(self, other):
		return Pos(self.row - other.row, self.col - other.col)
	
	def out_of_bounds(self):
		return self.row < 0 or self.row >= MAX_ROW or self.col < 0 or self.col >= MAX_COL


def get_2d(map, pos): return map[pos.row][pos.col]
def set_2d(map, pos, value): map[pos.row][pos.col] = value


@dataclass
class NodeCost:
	cost: int
	pos: Pos
	def __lt__(self, other): return self.cost < other.cost
	def __iter__(self):
		yield self.cost
		yield self.pos


data = []
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		data.append(list(map(ord, line.strip())))


MAX_ROW, MAX_COL = len(data), len(data[0])
DIR_UP, DIR_DOWN = Pos(-1, 0), Pos(1, 0)
DIR_LEFT, DIR_RIGHT = Pos(0, -1), Pos(0, 1)
START = None

end_list = []
for row, col in itertools.product(range(MAX_ROW), range(MAX_COL)):
	pos = Pos(row, col)
	if get_2d(data, pos) == ord('E'):
		set_2d(data, pos, ord('z'))
		START = pos
		
	elif get_2d(data, pos) == ord('S'):
		set_2d(data, pos, ord('a'))
		end_list.append(pos)

	elif get_2d(data, pos) == ord('a'):
		end_list.append(pos)


empty = [[False for _ in range(MAX_COL)] for _ in range(MAX_ROW)]
up, down, left, right = [deepcopy(empty) for _ in range(4)]

def _helper(map, pos, dir):
	new_pos = pos+dir
	if new_pos.out_of_bounds(): return False
	old_elevation, new_elevation = get_2d(map, pos), get_2d(map, new_pos)
	return new_elevation - old_elevation >= -1

for row, col in itertools.product(range(MAX_ROW), range(MAX_COL)):
	pos = Pos(row, col)
	set_2d(left, pos, _helper(data, pos, DIR_LEFT))
	set_2d(right, pos, _helper(data, pos, DIR_RIGHT))
	set_2d(up, pos, _helper(data, pos, DIR_UP))
	set_2d(down, pos, _helper(data, pos, DIR_DOWN))


def dijkstra():
	def _helper(pos, dir):
		new_pos = pos + dir
		if new_pos.out_of_bounds(): return False
		old_cost, new_cost = get_2d(costs, new_pos), node_cost + 1
		if new_cost < old_cost:
			heapq.heappush(min_cost, NodeCost(new_cost, new_pos))
			set_2d(costs, new_pos, new_cost)
			return True
		return False

	costs = [[INF for _ in range(MAX_COL)] for _ in range(MAX_ROW)]
	visited = set()
	set_2d(costs, START, 0)

	min_cost = [NodeCost(0, START)]
	while len(min_cost) != 0:
		node_cost, node_pos = heapq.heappop(min_cost)
		if node_pos in visited: continue
		visited.add(node_pos)

		if get_2d(up, node_pos): _helper(node_pos, DIR_UP)
		if get_2d(down, node_pos): _helper(node_pos, DIR_DOWN)
		if get_2d(left, node_pos): _helper(node_pos, DIR_LEFT)
		if get_2d(right, node_pos): _helper(node_pos, DIR_RIGHT)

	return costs

costs = dijkstra()
ans = INF
for pos in end_list:
	ans = min(ans, get_2d(costs, pos))
print(ans)