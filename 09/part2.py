def sgn(num):
	if num == 0: return 0
	elif num > 0: return 1
	else: return -1

def touching(x1, y1, x2, y2):
	return max(abs(x2 - x1), abs(y2 - y1)) < 2

class Node:
	def __init__(self, x=0, y=0):
		self.x, self.y = x, y
		self.parent, self.child = None, None

	def update(self):
		if self.parent:
			h_x, h_y = self.parent.x, self.parent.y # pos of "head"
			if not touching(h_x, h_y, self.x, self.y):
				if self.x != h_x: self.x += sgn(h_x - self.x)
				if self.y != h_y: self.y += sgn(h_y - self.y)

		if self.child:
			self.child.update()

dir_map = {
	'L': (-1, 0), 'R': (1, 0),
	'U': (0, 1), 'D': (0, -1)
}
visited = set([(0, 0)])

# doubly linked list (kinda)
rope, rope_len = [], 10
for i in range(rope_len): rope.append(Node())
for i in range(rope_len-1): rope[i].child = rope[i+1]
for i in range(1, rope_len): rope[i].parent = rope[i-1]
head, tail = rope[0], rope[-1]

with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		dir, length = line.strip().split(" ")
		length = int(length)
		dir_x, dir_y = dir_map[dir]

		for step in range(length):
			head.x += dir_x
			head.y += dir_y
			head.update()
			visited.add((tail.x, tail.y))
		
print(len(visited))