def min_max_input(instructions):
    x_min = 0
    x_max = 1000
    y_min = 0
    y_max = max((point[1]) for instruction in instructions for point in instruction) + 2
    return (x_min, x_max, y_min, y_max)


# returns list with x,y tuples
def parse_line(line):
    return [tuple(map(int, point.split(","))) for point in line.strip().split(" -> ")]


def print_field():
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


def add_sand():
    x = 500
    y = 0
    while True:
        if field[y][x-x_min] == "o":
            return False
        if field[y+1][x-x_min] == ".":
            y += 1
        else:
            if field[y+1][x-x_min-1] == ".":
                y += 1
                x -= 1
            elif field[y+1][x-x_min+1] == ".":
                y += 1
                x += 1
            else:
                field[y][x-x_min] = "o"
                return True


# parse file
with open("14/input.txt") as file:
    instructions = [parse_line(line) for line in file.readlines()]

# create field
x_min, x_max, y_min, y_max = min_max_input(instructions)
field = [["." for _ in range(x_min, x_max+1)] for _ in range(y_max+1)]
for line in instructions:
    for i in range(len(line)-1):
        add_rock_to_field(line[i], line[i+1])
add_rock_to_field((x_min, y_max), (x_max, y_max))

# drop sand
space_available = True
count = 0
while space_available:
    space_available = add_sand()
    if space_available:
        count += 1

print(count)
