from functools import reduce
from operator import __add__, __sub__, __mul__, __truediv__, __eq__

class Tree:
	def __init__(self, name):
		self.name = name
		self.children = []
		self.operator = None

	def add_child(self, child):
		self.children.append(child)
		
op_map = {
	"+": __add__,
	"-": __sub__,
	"*": __mul__,
	"/": __truediv__,
	"=": __eq__
}

def build_tree(cur="root"):
	content = data[cur]
	if cur == "humn":
		return None
	elif isinstance(content, int):
		return content
	else:
		T = Tree(cur)
		a, op_str, b = content
		T.operator = op_map[op_str]
		T.add_child(build_tree(a))
		T.add_child(build_tree(b))
		return T

def reduce_tree(T):
	is_num = True
	for c, child in enumerate(T.children):
		if child == None:
			return None

		if isinstance(child, (int, float)): continue

		reduced = reduce_tree(child)
		if reduced == None:
			is_num = False
		else:
			T.children[c] = reduced

	if is_num:
		return reduce(T.operator, T.children)
	else:
		return None

def inverse(expected, operator, num, first):
	if operator == __add__: return expected - num
	elif operator == __sub__:
		if first: # expected = ?? - num
			return expected + num
		else: # expected = num - ??
			return num - expected
	elif operator == __mul__: return expected / num
	else: # __truediv__
		if first: # expected = ?? / num
			return expected * num
		else: # expected = num / ??
			return num / expected

def solve(T):
	def _recurse(t, expected):
		if isinstance(t.children[0], Tree):
			new_t, num = t.children
			new_expected = inverse(expected, t.operator, num, True)
			return _recurse(new_t, new_expected)

		elif isinstance(t.children[1], Tree):
			new_t, num = t.children[::-1]
			new_expected = inverse(expected, t.operator, num, False)
			return _recurse(new_t, new_expected)

		else: # base case
			if t.children[0] == None:
				return inverse(expected, t.operator, t.children[1], True)
			else:
				return inverse(expected, t.operator, t.children[0], False)
	
	if isinstance(T.children[0], Tree):
		return _recurse(T.children[0], T.children[1])
	else:
		return _recurse(T.children[1], T.children[0])

	
data = {}
with open("./data.txt", "r") as fo:
	for c, line in enumerate(fo.readlines()):
		name = line[:4]
		content = line[6:].strip()

		if content.isdigit():
			data[name] = int(content)
		else:
			parsed = list(content.split(" "))
			if name == "root": parsed[1] = "="
			data[name] = parsed


T = build_tree()
reduce_tree(T)
ans = round(solve(T))
print(ans)