DIR_DOWN, DIR_LEFT, DIR_RIGHT = 0+1j, -1+1j, 1+1j
MAX_DEPTH = 160

def to_complex(s): return complex(*map(int, s.split(",")))
def intminmax(a, b): return int(min(a, b)), int(max(a, b))

rocks, sands = set(), set()
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		verts = list(map(to_complex, line.strip().split(" -> ")))
		prev = verts[0]
		for i in range(1, len(verts)):
			cur = verts[i]
			if (cur - prev).real == 0: # horizontal
				min_y, max_y = intminmax(prev.imag, cur.imag)
				for y in range(min_y, max_y+1): rocks.add(complex(cur.real, y))
			else: # vertical
				min_x, max_x = intminmax(prev.real, cur.real)
				for x in range(min_x, max_x+1): rocks.add(complex(x, cur.imag))
			prev = cur

while True:
	sand = 500+0j
	while True:
		if sand.imag == MAX_DEPTH: break # sand flows infinitely

		possible_pos = [sand+DIR_DOWN, sand+DIR_LEFT, sand+DIR_RIGHT]
		for pos in possible_pos:
			if pos not in sands and pos not in rocks:
				sand = pos
				break
		else: # all positions blocked
			break

	if sand.imag == MAX_DEPTH: break # sand flows infinitely
	sands.add(sand)
	
ans = len(sands)
print(ans)