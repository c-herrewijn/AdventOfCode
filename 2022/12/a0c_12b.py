import string


class Point:
    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.height = string.ascii_lowercase.find(height)
        self.fewest_steps = None

    def get_options(self):
        options = []
        if self.y > 0 and self.check_option(points[self.y-1][self.x]):
            options.append(points[self.y-1][self.x])
        if self.y < (len(points)-1) and self.check_option(points[self.y+1][self.x]):
            options.append(points[self.y+1][self.x])
        if self.x > 0 and self.check_option(points[self.y][self.x-1]):
            options.append(points[self.y][self.x-1])
        if self.x < len(points[0])-1 and self.check_option(points[self.y][self.x+1]):
            options.append(points[self.y][self.x+1])
        return options

    def check_option(self, point):
        if ((point.fewest_steps is None) or point.fewest_steps - 1 > self.fewest_steps) and \
                point.height - 1 <= self.height:
            return True


class Route:
    def __init__(self, points):
        self.points = points
        self.explored = False
        self.goal_reached = False

    def continue_route(self):
        while self.explored is False:
            self.next_step()

    def next_step(self):
        options = self.get_next_options()
        for option in options[1:]:
            self.create_parallel_route(option)
        if options:
            self.add_point(options[0])
        else:
            self.explored = True

    def get_last_point(self):
        return self.points[-1]

    def add_point(self, point):
        self.points.append(point)
        if point == end:
            self.goal_reached = True
            self.explored = True

    def get_next_options(self):  # also sets next step
        current_step = self.get_last_point().fewest_steps
        options = self.get_last_point().get_options()
        for option in options:
            option.fewest_steps = current_step + 1
        return options

    def create_parallel_route(self, option):
        new_route = Route([point for point in self.points])
        new_route.points.append(option)
        routes.append(new_route)


# parsing
points = []  # 2d-list [y][x]
with open("12/input.txt") as file:
    lines = file.readlines()
    for y, line in enumerate(lines):
        points.append([])
        for x in range(len(line.strip())):
            if line[x] == 'S':
                points[y].append(Point(x, y, 'a'))
            elif line[x] == 'E':
                end = Point(x, y, 'z')
                points[y].append(end)
            else:
                points[y].append(Point(x, y, line[x]))

# find route
start_locations = [p for line in points for p in line if p.x == 0]
steps = []
for start_point in start_locations:
    routes = []
    for i, _ in enumerate(points):
        for p in points[i]:
            p.fewest_steps = None
    start_point.fewest_steps = 0
    routes.append(Route([start_point]))
    while not all(route.explored for route in routes):
        unfinished_route = next(filter(lambda x: x.explored is False, routes))
        unfinished_route.continue_route()
    finished_routes = list(filter(lambda x: x.goal_reached, routes))
    if finished_routes:
        steps.append(finished_routes[0].points[-1].fewest_steps)

# result
print(sorted(steps)[0])
