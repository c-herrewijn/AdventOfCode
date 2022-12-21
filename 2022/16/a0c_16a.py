import re


class Route:
    def __init__(self, route):
        self.route = route
        self.time_left = 30
        self.finished = False

    def get_next_valves(self):
        pos = self.route[-1]
        return [i for i in range(len(valves)) if i not in self.route and dist[pos][i] < self.time_left]

    def score(self):
        minute = 30
        score = 0
        for s in range(len(self.route)-1):
            i = self.route[s]
            j = self.route[s+1]
            minute -= dist[i][j] + 1
            if minute <= 0:
                return score
            score += minute * flow_rates[valves[j]]
        return score


# used to parse data
def get_adjacent_valves(valve, trail):
    adjacent_valves = []
    for i in adj_lst[valve]:
        if i not in trail:
            if i in flow_rates.keys() or i == 'AA':
                adjacent_valves.append((i, 1))
            else:
                indirects = get_adjacent_valves(i, trail+[valve])
                for j in indirects:
                    adjacent_valves.append((j[0], j[1]+1))
    return adjacent_valves


def get_direct_distance(v1, v2):
    return next((v[1] for v in w_adj[v1] if v[0] == v2))


# parse data:
adj_lst = {}  # {'AA': ['BB', ..], ..}
flow_rates = {}  # {'CC': 1, ..}
with open("2022/16/input_test.txt") as file:
    for line in file:
        match = re.match(r"^Valve ([A-Z]+) has flow rate=([0-9]+); tunnels? leads? to valves? (.*)", line)
        name, flow_rate, adjecents = match.group(1), int(match.group(2)), list(match.group(3).split(", "))
        adj_lst.update({name: adjecents})
        if flow_rate != 0:
            flow_rates.update({name: flow_rate})

# calc weighted adjacencies per valve (only valves with flow rate and starting node AA)
w_adj = {'AA': get_adjacent_valves('AA', [])}  # {'AA': [('CC', 2), ..], ..}
for v in flow_rates.keys():
    w_adj.update({v: get_adjacent_valves(v, [])})

# create matrix with all distances between valves (using Flyod-Warshall algorith)
valves = sorted(list(w_adj.keys()))  # ['AA', ..]
dist = []
for i, fr in enumerate(valves):
    dist.append([])
    for to in valves:
        if fr == to:
            dist[i].append(0)
        elif to in (tup[0] for tup in w_adj[fr]):
            dist[i].append(get_direct_distance(fr, to))
        else:
            dist[i].append(999)
for k, _ in enumerate(valves):
    for i, _ in enumerate(valves):
        for j, _ in enumerate(valves):
            dist[i][j] = min((dist[i][j], dist[i][k] + dist[k][j]))

# find best path
routes = [Route([0])]
while True:
    route = next((r for r in routes if not r.finished), False)
    if not route:
        break
    next_options = route.get_next_valves()
    if not next_options:
        route.finished = True
    if len(next_options) > 1:
        cur_route = route.route.copy()
    for i, option in enumerate(next_options):
        if i == 0:
            route.route.append(option)
        else:
            routes.append(Route(cur_route.copy()+[option]))

print(max(r.score() for r in routes))
