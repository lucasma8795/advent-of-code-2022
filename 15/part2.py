from math import sqrt

SQRT_2 = sqrt(2)
EPS = 1e-7

def rotate_45deg(x, y): return (x-y)/SQRT_2, (x+y)/SQRT_2
def undo_rotate_45deg(x, y): return (x+y)/SQRT_2, (-x+y)/SQRT_2

x_pts, y_pts = [], []
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		s_x, s_y, b_x, b_y = map(int, line.strip().split(' '))
		r = abs(s_x - b_x) + abs(s_y - b_y) # manhattan distance

		# rotate points by 45 deg anticlockwise -> region becomes square
		s_x, s_y = rotate_45deg(s_x, s_y)
		b_x, b_y = rotate_45deg(b_x, b_y)
		
		d = r / SQRT_2 # half of side length = r * cos45

		x_pts.append(s_x - d)
		x_pts.append(s_x + d)
		y_pts.append(s_y - d)
		y_pts.append(s_y + d)

x_pts, y_pts = list(set(x_pts)), list(set(y_pts))
x_pts.sort()
y_pts.sort()

for i in range(len(x_pts)-1):
	if abs(abs(x_pts[i+1] - x_pts[i]) - SQRT_2) < EPS:
		x_min, x_max = x_pts[i], x_pts[i+1]
		break

for i in range(len(y_pts)-1):
	if abs(abs(y_pts[i+1] - y_pts[i]) - SQRT_2) < EPS:
		y_min, y_max = y_pts[i], y_pts[i+1]
		break

x_mid, y_mid = (x_min+x_max)/2, (y_min+y_max)/2
x_mid, y_mid = undo_rotate_45deg(x_mid, y_mid)
x_mid, y_mid = round(x_mid), round(y_mid)

ans = x_mid * 4000000 + y_mid
print(ans)