from sys import maxsize as INF
from collections import deque
from itertools import combinations

# "good" valves are non-zero valves & the AA valve
all_valves, good_valves = {}, []
flow_rates = [] # flow rates of "good" valves

def hash_valve(valve_str):
	if valve_str not in all_valves:
		all_valves[valve_str] = len(all_valves)
	return all_valves[valve_str]

# all combinations of n-bit nums with k bits set
def flip(num): return ~num & ((1<<len(good_valves))-1)
def find_bits(n):
	dp = [[[] for _ in range(i+1)] for i in range(n+1)]
	for i in range(1, n+1):
		dp[i][0].append(0)
	dp[1][1].append(1)
	for i in range(2, n+1):
		for j in range(1, i+1):
			dp[i][j] += [num + (1<<(i-1)) for num in dp[i-1][j-1]]
			if i != j: dp[i][j] += dp[i-1][j]
	return dp[n]

start = None
data = []
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		valve_str, flow_rate_str, neighbours_str = line.strip().split(" ")
		
		valve = hash_valve(valve_str)
		flow_rate = int(flow_rate_str)
		neighbours = map(hash_valve, neighbours_str.split(","))

		if valve_str == "AA": start = len(good_valves)
		if flow_rate != 0 or valve_str == "AA":
			good_valves.append(valve)
			flow_rates.append(flow_rate)
	
		data.append((valve, neighbours))
dp = find_bits(len(good_valves))

def build_graph(data, all_valves, good_valves):
	# floyd-warshall
	_G = [[INF for _ in range(len(all_valves))] for _ in range(len(all_valves))]
	for u, neighbours in data:
		for v in neighbours:
			_G[u][v] = 1
	for v in range(len(all_valves)): _G[v][v] = 0
	for k in range(len(all_valves)):
		for i in range(len(all_valves)):
			for j in range(len(all_valves)):
				if _G[i][j] > _G[i][k] + _G[k][j]:
					_G[i][j] = _G[i][k] + _G[k][j]
	# remove non-"good" vertices
	G = [[INF for _ in range(len(good_valves))] for _ in range(len(good_valves))]
	for i, u in enumerate(good_valves):
		for j, v in enumerate(good_valves):
			G[i][j] = _G[u][v] + 1 if u != v else 0 # +1 for time in opening valve
	return G

def solve(G, start, mask):
	ans = 0
	q = deque()
	q.append((start, 2**start, 26, 0, 0)) # cur node, visited, time left, total pressure, flow rate

	while q:
		u, visited, time, total_pressure, flow_rate = q.pop()
		ans = max(ans, total_pressure + time * flow_rate)

		for v in range(len(good_valves)):
			if mask & 1<<v == 0: continue # not in mask
			if visited & 1<<v != 0: continue # already visited
			if time - G[u][v] < 0: continue # not enough time

			new_visited = visited + 2**v # set v bit to 1
			new_time = time - G[u][v] # time - deltatime
			new_flow_rate = flow_rate + flow_rates[v] # add v flowrate
			new_total_pressure = total_pressure + flow_rate * G[u][v]
			q.append((v, new_visited, new_time, new_total_pressure, new_flow_rate))
		
	return ans

G = build_graph(data, all_valves, good_valves)

ans = 0
for self_mask in dp[7]:
	# print(self_mask)
	other_mask = flip(self_mask)
	ans = max(ans, solve(G, start, self_mask) + solve(G, start, other_mask))

print(ans)