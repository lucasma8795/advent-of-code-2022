from functools import cache

data = {}
with open("./data.txt", "r") as fo:
	for c, line in enumerate(fo.readlines()):
		name = line[:4]
		content = line[6:].strip()

		if content.isdigit():
			data[name] = int(content)
		else:
			data[name] = content.split(" ")

@cache
def solve(name):
	content = data[name]
	if isinstance(content, int):
		return content
	else:
		a, op, b = content
		if op == "+": return solve(a) + solve(b)
		elif op == "-": return solve(a) - solve(b)
		elif op == "*": return solve(a) * solve(b)
		elif op == "/": return solve(a) / solve(b)

ans = round(solve("root"))
print(ans)