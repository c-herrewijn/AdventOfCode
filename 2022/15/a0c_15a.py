import re


class Sensor:
    def __init__(self, s_x, s_y, b_x, b_y):
        self.x = s_x
        self.y = s_y
        self.range = abs(s_x - b_x) + abs(s_y - b_y)

    def __repr__(self):
        return f"{self.x}, {self.y}, {self.range}"


# parse file
sensors = []
with open("2022/15/input.txt") as file:
    for line in file:
        match = re.match(r"^Sensor at x=(-?[0-9]+), y=(-?[0-9]+): closest beacon is at x=(-?[0-9]+), y=(-?[0-9]+)", line)
        s_x, s_y, b_x, b_y = match.group(1), match.group(2), match.group(3), match.group(4)
        sensors.append(Sensor(int(s_x), int(s_y), int(b_x), int(b_y)))

# result
local_x_min = min(sensor.x - (sensor.range - abs(sensor.y - 2000000)) for sensor in sensors)
local_x_max = max(sensor.x + (sensor.range - abs(sensor.y - 2000000)) for sensor in sensors)
print(local_x_max - local_x_min)
