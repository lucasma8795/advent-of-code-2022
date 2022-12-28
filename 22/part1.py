def left(dr, dc): return -dc, dr
def right(dr, dc): return dc, -dr
def wrap(a, b, n): return (n-a)%(b-a)+a

SIZE = 50
r, c = 0, SIZE*2
dr, dc = 0, 1
def get_x_border(y):
	if 	 0      <= y < SIZE: 	return SIZE, 	SIZE*3
	elif SIZE   <= y < SIZE*2: 	return SIZE,	SIZE*2
	elif SIZE*2 <= y < SIZE*3: 	return 0,		SIZE*2
	elif SIZE*3 <= y < SIZE*4: 	return 0,		SIZE
def get_y_border(x):
	if 	 0      <= x < SIZE: 	return SIZE*2, 	SIZE*4
	elif SIZE   <= x < SIZE*2: 	return 0, 		SIZE*3
	elif SIZE*2 <= x < SIZE*3: 	return 0,		SIZE

instructions = []
with open("./instructions.txt", "r") as fo:
	for line in fo.readlines():
		line = line.strip()
		if line.isdigit(): line = int(line)
		instructions.append(line)

data = []
char_map = {' ': -1, '.': 0, '#': 1}
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		data.append(list(map(char_map.__getitem__, line.strip("\n") + ' '*(16 - len(line.strip("\n"))))))

for instr in instructions:
	if isinstance(instr, int):
		for _ in range(instr):
			new_r, new_c = r+dr, c+dc
			if new_r == r:
				min_x, max_x = get_x_border(r)
				new_c = wrap(min_x, max_x, new_c)
			else:
				min_y, max_y = get_y_border(c)
				new_r = wrap(min_y, max_y, new_r)

			if data[new_r][new_c] == 1: break
			r, c = new_r, new_c
	
	else:
		if instr == "L": dr, dc = left(dr, dc)
		else: dr, dc = right(dr, dc)

ans = 0
if dr == -1 and dc == 0: ans += 1
elif dr == 0 and dc == -1: ans += 2
elif dr == 1 and dc == 0: ans += 3
ans += 1000 * (r+1) + 4 * (c+1)
print(ans)