from math import lcm
lines = []
BLOCK_LEN = 4

class Monkey:
	def __init__(self, items, div_cond, throw_true, throw_false, operation):
		self.items = items
		self.div_cond = div_cond
		self.throw_true = throw_true
		self.throw_false = throw_false
		self.items_inspected = 0
		
		operator, operand = operation
		operand = int(operand)
		self.operation = operation
		if operator == '+':
			self.transform_func = lambda x: x + operand
		elif operator == '*':
			self.transform_func = lambda x: x * operand
		elif operator == "**":
			self.transform_func = lambda x: x ** operand


all_items = []
monkeys = []
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		lines.append(line.strip())
		if len(lines) == BLOCK_LEN:
			items = list(map(int, lines[0].split(" ")))
			all_items += items
			operation = lines[1].split(" ")
			div_cond = int(lines[2])
			throw_true, throw_false = map(int, lines[3].split(" "))
			monkeys.append(Monkey(items, div_cond, throw_true, throw_false, operation))
			lines = []

MOD = lcm(*all_items)

for round in range(10000):
	for c, monkey in enumerate(monkeys):
		while len(monkey.items) != 0:
			item = monkey.items.pop()
			monkey.items_inspected += 1
			item = monkey.transform_func(item) % MOD
			if item % monkey.div_cond == 0:
				monkeys[monkey.throw_true].items.append(item)
			else:
				monkeys[monkey.throw_false].items.append(item)

items_inspected = [monkey.items_inspected for monkey in monkeys]
items_inspected.sort(reverse=True)
ans = items_inspected[0] * items_inspected[1]
print(ans)