import re


class Valve:
    def __init__(self, name, rate, path_to_valves):
        self.name = name
        self.rate = rate
        self.path_to_valves = path_to_valves
        self.turns_of_flow = 0
        self.score = 0

    def __repr__(self):
        return self.name


valves = {}
with open("2022/16/input_test.txt") as file:
    for line in file:
        match = re.match(r"^Valve ([A-Z]+) has flow rate=([0-9]+); tunnels? leads? to valves? (.*)", line)
        if match:
            valves.update({match.group(1): Valve(match.group(1), int(match.group(2)), list(match.group(3).split(", ")))})


print(list(valves.keys()))
print(valves['CC'])
print(valves['CC'].rate)
print(valves['CC'].path_to_valves)
