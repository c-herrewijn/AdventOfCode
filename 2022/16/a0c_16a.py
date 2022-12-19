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
    def __init__(self, valve, open, minute, score):
        self.valve = valve  # valve object
        self.open = open
        self.minute = minute
        self.score = score  # based on all open Valves, and the remaining minutes
        self.finished = False

    def __repr__(self):
        return f"valve {self.valve}, open: {self.open}, minute {self.minute}, score = {self.score}, finished = {self.finished}"

    def add_next_states(self):
        if self.minute < 30:
            if self.open == 0 and self.valve.flow_rate != 0:
                states.append(State(self.valve, 1, self.minute + 1, calc_score(self.score, self.minute + 1, self.valve.flow_rate)))
            
            # only add next state if there is no exiting state that is better or equal on both time AND score
            for next_valve in self.valve.next_valves:
                if not next((s for s in states if s.valve == next_valve and s.score >= self.score and s.minute <= self.minute + 1), False):
                    states.append(State(next_valve, 0, self.minute + 1, self.score))

                # put inferior states to finished
                for s in states:
                    if s.finished == False and s.valve == next_valve and s.score < self.score and s.minute > self.minute + 1:
                        s.finished == True

        self.finished = True


def calc_score(start_score, minute, flow_rate):
    return start_score + (30 - minute) * flow_rate 


# parse data
valves = {}
with open("2022/16/input_test.txt") as file:
    for line in file:
        match = re.match(r"^Valve ([A-Z]+) has flow rate=([0-9]+); tunnels? leads? to valves? (.*)", line)
        if match:
            valves.update({match.group(1): Valve(match.group(1), int(match.group(2)), list(match.group(3).split(", ")))})
for valve in valves.values():
    valve.next_valves = [valves[i] for i in valve.next_valves_str]
        

# explore routes
states = []
minute = 30
states.append(State(valves['AA'], 0, 0, 0))
while True:
    unfinished_state = next((s for s in states if s.finished == False), False)
    if unfinished_state:
        unfinished_state.add_next_states()
    else:
        break


# test
for s in states:
    print(s)

print("--")
next((s for s in states if s.finished == False)).add_next_states()
for s in states:
    print(s)



# class Route:
#     def init(self):
#         self.actions = []
#         self.finished = 0

# class Action:
#     def init(self):
#         self.start_valve
#         self.go_to_valve
#         self.open_valve
#         self.start_state
#         self.minute
#         self.score  # based on all open Valves, and the remaining minutes
