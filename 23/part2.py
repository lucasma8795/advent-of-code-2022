elves = set()
with open("./data.txt", "r") as fo:
	for r, line in enumerate(fo.readlines()):
		for c, char in enumerate(line.strip()):
			if char == "#": elves.add((r, c))
	
priority = "nswe"
round = 1

while True:
	proposed = {}
	new_elves = set()
	changed = False

	for pos in elves:
		r, c = pos
		n, ne = (r-1, c), (r-1, c+1)
		e, se = (r, c+1), (r+1, c+1)
		s, sw = (r+1, c), (r+1, c-1)
		w, nw = (r, c-1), (r-1, c-1)

		if len(set((n, e, s, w, ne, se, sw, nw)) & elves) == 0:
			new_elves.add(pos)
			continue

		check = {
			"n": (n, set((n, ne, nw))),
			"s": (s, set((s, se, sw))),
			"w": (w, set((w, nw, sw))),
			"e": (e, set((e, ne, se)))
		}

		for p in priority:
			dir, adj = check[p]
			if len(adj & elves) == 0:
				changed = True
				if dir in proposed:
					proposed[dir].append(pos)
				else:
					proposed[dir] = [pos]
				break
		else:
			new_elves.add(pos)

	for k, v in proposed.items():
		if len(v) == 1:
			new_elves.add(k)
		else:
			for i in v: new_elves.add(i)
	
	if not changed:
		print(round)
		exit()

	elves = new_elves
	priority = priority[1:] + priority[0]
	round += 1