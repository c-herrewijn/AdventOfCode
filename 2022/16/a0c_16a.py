import re
import copy


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

    def __repr__(self):
        return f"\nvalve {self.valve}, open: {self.open}, minute {self.minute}, score = {self.score}"


class Route:
    def __init__(self, states):
        self.states = states
        self.finished = False

    def __repr__(self):
        # return f"states {self.states}, finised: {self.finished}"
        return f"score {self.get_score()}, finised: {self.finished}, states {self.states}\n"

    def valve_open(self, valve):
        return any(state.open for state in self.states if state.valve.name == valve.name)

    def add_state(self, state):
        self.states.append(state)

    def get_score(self):
        return self.states[-1].score

    def get_next_states(self):
        next_states = []
        lst_state = self.states[-1]

        if lst_state.minute < 30:
            if not lst_state.open and lst_state.valve.flow_rate != 0:
                next_states.append(State(
                    lst_state.valve,
                    True,
                    lst_state.minute + 1,
                    calc_score(lst_state.score, lst_state.minute + 1, lst_state.valve.flow_rate)))

            # only add next state if there is no exiting state that is better or equal on both time AND score
            for next_valve in lst_state.valve.next_valves:
                # if self == routes[0]:
                #     print(f"minute {routes[0].states[-1].minute}")
                # for s in states:
                #     if s.valve == next_valve and s.score >= lst_state.score and s.minute <= lst_state.minute + 1:
                #         pass
                if not next((s for s in states if s.valve == next_valve and s.score >= lst_state.score and s.minute <= lst_state.minute + 1), False):
                    new_state = State(
                        next_valve,
                        self.valve_open(next_valve),
                        lst_state.minute + 1,
                        lst_state.score)
                    next_states.append(new_state)
        return next_states


def calc_score(start_sore, minute, flow_rate):
    return start_sore + (30 - minute) * flow_rate


# parse data
valves = {}
routes = []
states = []
with open("2022/16/input.txt") as file:
    for line in file:
        match = re.match(r"^Valve ([A-Z]+) has flow rate=([0-9]+); tunnels? leads? to valves? (.*)", line)
        if match:
            valves.update({match.group(1): Valve(match.group(1), int(match.group(2)), list(match.group(3).split(", ")))})
for valve in valves.values():
    valve.next_valves = [valves[i] for i in valve.next_valves_str]

# explore routes
states.append(State(valves['AA'], False, 0, 0))
routes.append(Route([states[0]]))
while not all(r.finished for r in routes):

    unfinished_route = next((r for r in routes if not r.finished))
    new_states = unfinished_route.get_next_states()
    states.extend(new_states)

    # create new routes
    if len(new_states) > 1:
        for state in new_states[1:]:
            new_statelist = copy.deepcopy(unfinished_route.states)
            new_statelist.append(state)
            routes.append(Route(new_statelist))

    # extend current route
    if new_states:
        unfinished_route.states.append(new_states[0])
    else:
        unfinished_route.finished = True


print(max((r.get_score() for r in routes)))
# 1610 too low
