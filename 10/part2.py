from sys import stdout
cycle, x = 0, 1

def draw(pos, x, cycle):
	if abs(pos-x) <= 1: stdout.write('#')
	else: stdout.write('.')
	if cycle % 40 == 39: stdout.write('\n')

with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		cmds = line.strip().split(" ")

		match cmds[0]:
			case "noop":
				draw(cycle%40, x, cycle)
				cycle += 1

			case "addx":
				num = int(cmds[1])
				draw(cycle%40, x, cycle)
				cycle += 1
				draw(cycle%40, x, cycle)
				cycle += 1
				x += num

stdout.flush()