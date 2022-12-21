import re


class Valve:
    def __init__(self, name, flow_rate, next_valves_str):
        self.name = name
        self.flow_rate = flow_rate
        self.next_valves_str = next_valves_str  # strings
        self.next_valves = []  # objects

    def __repr__(self):
        return self.name


class State:
    def __init__(self, position, open, minute, score):
        self.position = position  # valve object
        self.open = open  # set with open valve objects
        self.minute = minute
        self.score = score  # based on all open Valves, and the remaining minutes
        self.finished = False

    def __repr__(self):
        return f"\nposition {self.position}, open: {self.open}, minute {self.minute}, score = {self.score}"

    def get_next_states(self):
        next_states = []
        if self.minute < 30:
            if self.position not in self.open and self.position.flow_rate != 0:
                open_valves = self.open.copy()
                open_valves.add(self.position)
                next_states.append(State(
                    self.position,
                    open_valves,
                    self.minute + 1,
                    calc_score(self.score, self.minute + 1, self.position.flow_rate)))

            # only add state if there is no exiting state that is better or equal on all: time, score AND open valves
            # NOTE: fewer open valves is better since it has more opportunity to increase the score later on
            for next_valve in self.position.next_valves:
                if not next((s for s in states if
                            s.position == next_valve and
                            s.score >= self.score and
                            s.minute <= self.minute + 1 and
                            s.open.issubset(self.open)), False):
                    new_state = State(next_valve, self.open, self.minute + 1, self.score)
                    next_states.append(new_state)
        return next_states


def calc_score(start_sore, minute, flow_rate):
    return start_sore + (30 - minute) * flow_rate


# parse data
valves = {}
states = []
with open("2022/16/input.txt") as file:
    for line in file:
        match = re.match(r"^Valve ([A-Z]+) has flow rate=([0-9]+); tunnels? leads? to valves? (.*)", line)
        if match:
            valves.update({match.group(1): Valve(match.group(1),
                          int(match.group(2)),
                          list(match.group(3).split(", ")))})
for valve in valves.values():
    valve.next_valves = [valves[i] for i in valve.next_valves_str]

# explore routes
states.append(State(valves['AA'], set(), 0, 0))
while not all(s.finished for s in states):
    unfinished_state = next((s for s in states if not s.finished))
    new_states = unfinished_state.get_next_states()
    unfinished_state.finished = True
    states.extend(new_states)

print(max((s.score for s in states)))
