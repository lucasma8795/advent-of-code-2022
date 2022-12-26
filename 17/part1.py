# 	0	1	2	3	4	5	6	7
#	8	9	10	11	12	13	14	15
# 	16	17	18	19	20	21	22	23
# 	24	25	26	27	28	29	30	31
# chamber is 7 units wide; discard 0, 8, 16, 24 bits

ROCKS = [			# represent rocks as u32 ints
	0x78000000,		# 27, 28, 29, 30
	0x10381000,		# 12, 19, 20, 21, 28
	0x38202000,		# 13, 21, 27, 28, 29
	0x08080808,		# 3, 11, 19, 27
	0x18180000		# 19, 20, 27, 28
]
HEIGHTS = [1, 3, 3, 4, 2]
LEFT_WALL = 0x2020202
RIGHT_WALL = 0x80808080

def move(rock, is_left):
	if is_left:
		if rock & LEFT_WALL == 0:
			rock >>= 1
	else:
		if rock & RIGHT_WALL == 0:
			rock <<= 1
	return rock

def add_to_chamber(chamber, rock, y):
	chamber[y+3] |= 0xFF & rock
	chamber[y+2] |= 0xFF & rock>>8
	chamber[y+1] |= 0xFF & rock>>16
	chamber[y]   |= 0xFF & rock>>24

def view_chamber(y):
	return chamber[y+3] | chamber[y+2]<<8 | chamber[y+1]<<16 | chamber[y]<<24

# store chamber as a list of u8 ints
chamber = [0] * 10000
height = 0

with open("./data.txt", "r") as fo:
	data = fo.read().strip()
data_ptr = 0

for i in range(2022):
	rock = ROCKS[i%5]
	y = height + 3

	while True:
		# move rock left/right
		is_left = data[data_ptr%len(data)] == "<"
		data_ptr += 1
		moved_rock = move(rock, is_left)
		if moved_rock & view_chamber(y) == 0:
			rock = moved_rock

		# move rock down
		if y == 0:
			add_to_chamber(chamber, rock, y)
			break
		window = view_chamber(y-1)
		if window & rock != 0:
			add_to_chamber(chamber, rock, y)
			break
		y -= 1

	height = max(height, y+HEIGHTS[i%5])
	
print(height)