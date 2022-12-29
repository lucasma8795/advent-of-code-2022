data = []
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		data.append(line.strip())

WIDTH, HEIGHT = len(data[0]), len(data)
START, END = (0, -1), (HEIGHT, WIDTH-1)

def solve(start, end, time=0):
	pos = set([start])
	while True:
		new_pos = set()
		for r, c in pos:
			for new_r, new_c in [(r, c), (r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
				if (new_r, new_c) == end:
					return time
		
				if not 0 <= new_r < HEIGHT or not 0 <= new_c < WIDTH: continue
				if data[(new_r - time) % HEIGHT][new_c] != "v" and \
					data[(new_r + time) % HEIGHT][new_c] != "^" and \
					data[new_r][(new_c - time) % WIDTH] != ">" and \
					data[new_r][(new_c + time) % WIDTH] != "<":
					new_pos.add((new_r, new_c))

		if len(new_pos) != 0: pos = new_pos
		time += 1

ans = solve(START, END, solve(END, START, solve(START, END)))
print(ans)