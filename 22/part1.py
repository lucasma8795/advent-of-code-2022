def left(dr, dc): return -dc, dr
def right(dr, dc): return dc, -dr
def wrap(a, b, n): return (n-a)%(b-a)+a

SIZE = 50
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
		instructions.append(line.strip())

data = []
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		data.append(list(line.strip("\n").ljust(SIZE*4)))

r, c = 0, SIZE
dr, dc = 0, 1
for instr in instructions:
	match instr:
		case "L": dr, dc = left(dr, dc)
		case "R": dr, dc = right(dr, dc)
		case _:
			for _ in range(int(instr)):
				new_r, new_c = r+dr, c+dc
				if new_r == r:
					min_x, max_x = get_x_border(r)
					new_c = wrap(min_x, max_x, new_c)
				else:
					min_y, max_y = get_y_border(c)
					new_r = wrap(min_y, max_y, new_r)

				if data[new_r][new_c] == '#': break
				r, c = new_r, new_c

ans = 0
if dr == 1 and dc == 0: ans += 1
elif dr == 0 and dc == -1: ans += 2
elif dr == -1 and dc == 0: ans += 3
ans += 1000 * (r+1) + 4 * (c+1)
print(ans)