cycle, x = 1, 1
strengths = []

with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		cmds = line.strip().split(" ")

		match cmds[0]:
			case "noop":
				cycle += 1

			case "addx":
				num = int(cmds[1])
				if (cycle + 20) % 40 == 39:
					strengths.append((cycle+1) * x)
				x += num
				cycle += 2
				
		if (cycle + 20) % 40 == 0:
			strengths.append(cycle * x)

print(sum(strengths))