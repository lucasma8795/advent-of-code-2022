from json import loads

lines = []
data = []
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		lines.append(line)
		if len(lines) == 2:
			data.append([loads(lines[0]), loads(lines[1])])
			lines = []

def is_in_order(left, right):
	left_isint = isinstance(left, int)
	right_isint = isinstance(right, int)

	if left_isint and right_isint:
		if left < right: return True
		elif left > right: return False
		else: return None
	
	if left_isint: return is_in_order([left], right)
	if right_isint: return is_in_order(left, [right])

	for i in range(min(len(left), len(right))):
		res = is_in_order(left[i], right[i])
		if res is not None: return res
	
	if len(left) < len(right): return True
	elif len(left) > len(right): return False
	return None

ans = 0
for c, pair in enumerate(data):
	left, right = pair
	if is_in_order(left, right): ans += c+1

print(ans)