from sys import maxsize as INF

# "good" valves are non-zero valves & the AA valve
all_valves, good_valves = {}, []
flow_rates = [] # flow rates of "good" valves

def hash_valve(valve_str):
	if valve_str not in all_valves:
		all_valves[valve_str] = len(all_valves)
	return all_valves[valve_str]

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

def solve(G, u, visited, time=30, total_pressure=0, flow_rate=0):
	ans = 0
	more = False
	for v in range(len(good_valves)):
		if visited & 2**v != 0: continue # already visited
		if time - G[u][v] < 0: continue # not enough time
		more = True
		ans = max(ans, solve(G, v, visited+2**v, 
			time=time-G[u][v],
			total_pressure=total_pressure+flow_rate*G[u][v],
			flow_rate=flow_rate+flow_rates[v]
		))
	if more: return ans
	else: return total_pressure + time * flow_rate

G = build_graph(data, all_valves, good_valves)
ans = solve(G, start, 2**start)
print(ans)