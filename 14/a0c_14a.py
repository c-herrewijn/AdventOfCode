def min_max_input(instructions):
    x_min = min((point[0]) for instruction in instructions for point in instruction)
    x_max = max((point[0]) for instruction in instructions for point in instruction)
    y_min = min((point[1]) for instruction in instructions for point in instruction)
    y_max = max((point[1]) for instruction in instructions for point in instruction)
    return (x_min, x_max, y_min, y_max)


# returns list with x,y tuples
def parse_line(line):
    return [tuple(map(int, point.split(","))) for point in line.strip().split(" -> ")]


def print_field(field):
    for y in range(y_max + 1):
        for x in range(x_min, x_max + 1):
            print(field[y][x-x_min], end="")
        print()


def add_rock_to_field(r_start, r_end):
    x_coords = (r_start[0]-x_min, r_end[0]-x_min)
    y_coords = (r_start[1], r_end[1])
    for x in range(min(x_coords), max(x_coords)+1):
        for y in range(min(y_coords), max(y_coords)+1):
            field[y][x] = "#"

# parse file
with open("14/input_test.txt") as file:
    instructions = [parse_line(line) for line in file.readlines()]

# create field
x_min, x_max, y_min, y_max = min_max_input(instructions)
field = [["." for _ in range(x_min, x_max+1)] for _ in range(y_max+1)]
for line in instructions:
    for i in range(len(line)-1):
        add_rock_to_field(line[i], line[i+1])

print_field(field)
