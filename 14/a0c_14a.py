def min_max_input(instructions):
    x_min = min((point[0]) for instruction in instructions for point in instruction)
    x_max = max((point[0]) for instruction in instructions for point in instruction)
    y_min = min((point[1]) for instruction in instructions for point in instruction)
    y_max = max((point[1]) for instruction in instructions for point in instruction)
    return (x_min, x_max, y_min, y_max)


# returns list with x,y tuples
def parse_line(line):
    return [tuple(point.split(",")) for point in line.strip().split(" -> ")]


field = []
with open("14/input_test.txt") as file:
    instructions = [parse_line(line) for line in file.readlines()]
    x_min, x_max, y_min, y_max = min_max_input(instructions)

    print(x_min)
    print(x_max)
    print(y_min)
    print(y_max)
