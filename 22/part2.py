def left(dr, dc): return -dc, dr
def right(dr, dc): return dc, -dr
def wrap(r, c, dr, dc):
	match r//SIZE, c//SIZE, dr, dc:
		case  -1,  1, -1,  0:	return  c+SIZE*2,	0,			0,	1
		case   3, -1,  0, -1:	return  0, 			r-SIZE*2,	1,  0
		case  -1,  2, -1,  0:	return  SIZE*4-1,	c-SIZE*2,	-1,  0
		case   4,  0,  1,  0:	return  0, 			c+SIZE*2, 	1,  0
		case   0,  3,  0,  1:	return  SIZE*3-r-1,	SIZE*2-1,	0, -1 
		case   2,  2,  0,  1:	return  SIZE*3-r-1, SIZE*3-1,	0, -1
		case   1,  2,  1,  0:	return  c-SIZE, 	SIZE*2-1,	0, -1
		case   1,  2,  0,  1:	return  SIZE-1, 	r+SIZE, 	-1,  0
		case   3,  1,  1,  0:	return  c+SIZE*2, 	SIZE-1,  	0, -1
		case   3,  1,  0,  1:	return  SIZE*3-1, 	r-SIZE*2,	-1,  0
		case   2, -1,  0, -1:	return  SIZE*3-r-1, SIZE, 		0,  1
		case   0,  0,  0, -1:	return  SIZE*3-r-1, 0,			0,  1
		case   1,  0, -1,  0:	return  c+SIZE, 	SIZE, 		0,  1
		case   1,  0,  0, -1:	return  SIZE*2, 	r-SIZE,		1,  0

SIZE = 50
def out_of_bounds(r, c):
	match r//SIZE, c//SIZE:
		case 0, 1: return False
		case 0, 2: return False
		case 1, 1: return False
		case 2, 0: return False
		case 2, 1: return False
		case 3, 0: return False
		case _, _: return True

instructions = []
with open("./instructions.txt", "r") as fo:
	for line in fo.readlines():
		instructions.append(line.strip())

data = []
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		data.append(list(line.strip("\n").ljust(SIZE*3)))

r, c = 0, SIZE
dr, dc = 0, 1
for instr in instructions:
	match instr:
		case "L": dr, dc = left(dr, dc)
		case "R": dr, dc = right(dr, dc)
		case _:
			for _ in range(int(instr)):
				new_r, new_c, new_dr, new_dc = r+dr, c+dc, dr, dc
				if out_of_bounds(new_r, new_c):
					new_r, new_c, new_dr, new_dc = wrap(new_r, new_c, dr, dc)
				if data[new_r][new_c] == '#': break
				r, c, dr, dc = new_r, new_c, new_dr, new_dc

ans = 0
if dr == 1 and dc == 0: ans += 1
elif dr == 0 and dc == -1: ans += 2
elif dr == -1 and dc == 0: ans += 3
ans += 1000 * (r+1) + 4 * (c+1)
print(ans)