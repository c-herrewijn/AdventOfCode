import re


def get_adjacent_valves(valve, trail):
    adjacent_valves = []
    for i in adj_lst[valve]:
        if i not in trail:
            if i in flow_rates.keys():
                adjacent_valves.append((i, 1))
            else:
                indirects = get_adjacent_valves(i, trail+[valve])
                for j in indirects:
                    adjacent_valves.append((j[0], j[1]+1))
    return adjacent_valves


# parse data:
adj_lst = {}
flow_rates = {}
with open("2022/16/input_test2.txt") as file:
    for line in file:
        match = re.match(r"^Valve ([A-Z]+) has flow rate=([0-9]+); tunnels? leads? to valves? (.*)", line)
        name, flow_rate, adjecents = match.group(1), int(match.group(2)), list(match.group(3).split(", "))
        adj_lst.update({name: adjecents})
        if flow_rate != 0:
            flow_rates.update({name: flow_rate})

# create weighted adjacency list (only valves with flow rate and starting node AA)
w_adj_lst = {'AA': get_adjacent_valves('AA', [])}
for v in flow_rates.keys():
    w_adj_lst.update({v: get_adjacent_valves(v, [])})
