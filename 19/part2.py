from functools import cache

data = []
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		args = list(map(int, line.strip().split(" ")))
		ore_cost = args[0]
		clay_cost = args[1]
		obsidian_cost = (args[2], args[3])
		geode_cost = (args[4], args[5])
		data.append((ore_cost, clay_cost, obsidian_cost, geode_cost))

def solve(id, ore_cost, clay_cost, obsidian_cost, geode_cost):
	best = 0
	nodes_explored = 0
	
	@cache
	def _recurse(
		ore=0, clay=0, obsidian=0, geode=0,
		ore_robots=1, clay_robots=0, obsidian_robots=0, geode_robots=0,
		time=32
	):
		nonlocal nodes_explored
		nonlocal best

		nodes_explored += 1
		# base case: time=0
		if time == 0:
			best = max(best, geode)
			return

		# robot logic
		ore += ore_robots
		clay += clay_robots
		obsidian += obsidian_robots
		geode += geode_robots
	
		# pruning
		upper_bound = geode + geode_robots * time + time * (time-1) // 2
		if upper_bound < best: return

		# build geode robot
		if ore-ore_robots >= geode_cost[0] and obsidian-obsidian_robots >= geode_cost[1]:
			_recurse(
				ore-geode_cost[0], clay, obsidian-geode_cost[1], geode,
				ore_robots, clay_robots, obsidian_robots, geode_robots+1,
				time-1
			)
		
		# build obsidian robot
		if ore-ore_robots >= obsidian_cost[0] and clay-clay_robots >= obsidian_cost[1]:
			_recurse(
				ore-obsidian_cost[0], clay-obsidian_cost[1], obsidian, geode,
				ore_robots, clay_robots, obsidian_robots+1, geode_robots,
				time-1
			)
		
		# build clay robot
		if ore-ore_robots >= clay_cost:
			_recurse(
				ore-clay_cost, clay, obsidian, geode,
				ore_robots, clay_robots+1, obsidian_robots, geode_robots,
				time-1
			)
		
		# build ore robot
		if ore-ore_robots >= ore_cost:
			_recurse(
				ore-ore_cost, clay, obsidian, geode,
				ore_robots+1, clay_robots, obsidian_robots, geode_robots,
				time-1
			)
		
		# do nothing
		_recurse(
			ore, clay, obsidian, geode,
			ore_robots, clay_robots, obsidian_robots, geode_robots, 
			time-1
		)

	_recurse()
	return id * best

ans = 1
for id, costs in enumerate(data[:3]):
	ans *= solve(1, *costs)
print(ans)