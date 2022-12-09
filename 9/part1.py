def touching(x1, y1, x2, y2):
	x_diff, y_diff = abs(x2 - x1), abs(y2 - y1)
	return x_diff == y_diff == 1 or x_diff + y_diff < 2

dir_map = {
	'L': (-1, 0), 'R': (1, 0),
	'U': (0, 1), 'D': (0, -1)
}
h_x, h_y = 0, 0 # pos of head
t_x, t_y = 0, 0 # pos of tail
h_prevx, h_prevy = 0, 0 # prev pos of head

visited = set([(0, 0)])
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		dir, length = line.strip().split(" ")
		dir_x, dir_y = dir_map[dir]
		length = int(length)

		for step in range(length):
			h_prevx, h_prevy = h_x, h_y
			h_x += dir_x
			h_y += dir_y

			if touching(h_x, h_y, t_x, t_y): continue
				
			t_x, t_y = h_prevx, h_prevy
			visited.add((t_x, t_y))

print(len(visited))