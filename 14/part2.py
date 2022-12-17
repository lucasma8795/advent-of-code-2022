from functools import cache

DIR_UP, DIR_LEFT, DIR_RIGHT = 0-1j, -1-1j, 1-1j

def to_complex(s): return complex(*map(int, s.split(",")))
def intminmax(a, b): return int(min(a, b)), int(max(a, b))
def out_of_bounds(pos): return not 500-pos.imag <= pos.real <= 500+pos.imag

@cache
def is_blocked(pos):
	if pos == 500+0j: return False

	possible_pos = [pos+DIR_UP, pos+DIR_LEFT, pos+DIR_RIGHT]
	possible_pos = [pos for pos in possible_pos if not out_of_bounds(pos)]

	for pos in possible_pos:
		if pos in rocks: continue
		if not is_blocked(pos): return False
	return True

max_depth = 0
rocks = set()
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		verts = list(map(to_complex, line.strip().split(" -> ")))
		prev = verts[0]
		for i in range(1, len(verts)):
			cur = verts[i]
			if (cur - prev).real == 0: # horizontal
				min_y, max_y = intminmax(prev.imag, cur.imag)
				max_depth = max(max_depth, max_y)
				for y in range(min_y, max_y+1): rocks.add(complex(cur.real, y))
			else: # vertical
				min_x, max_x = intminmax(prev.real, cur.real)
				for x in range(min_x, max_x+1): rocks.add(complex(x, cur.imag))
			prev = cur

blocked = set()
for y in range(max_depth+1, 0, -1):
	for x in range(500-y, 500+y+1):
		pos = complex(x, y)
		if pos in rocks: continue
		if is_blocked(pos):
			blocked.add(pos)

ans = (max_depth+2) ** 2 - len(blocked) - len(rocks)
print(ans)