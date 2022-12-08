def is_vis_north(f, x, y):
    return all(f[i][x] < f[y][x] for i in range(y))

def is_vis_south(f, x, y, y_max):
    return all(f[i][x] < f[y][x] for i in range(y+1, y_max))

def is_vis_west(f, x, y):
    return all(f[y][i] < f[y][x] for i in range(x))

def is_vis_east(f, x, y, x_max):
    return all(f[y][i] < f[y][x] for i in range(x+1, x_max))

def is_visible(f, x, y, x_max, y_max):
    return is_vis_north(f, x, y) or is_vis_south(f, x, y, y_max) or is_vis_west(f, x, y) or is_vis_east(f, x, y, x_max)

f = []
with open("08/input.txt") as file:
    for y, line in enumerate(file):
        f.append([])
        for c in line.strip():
            f[y].append(int(c))

    y_max = len(f)
    x_max = len(f[0])
    print(sum(is_visible(f, x, y, x_max, y_max) for x in range(x_max) for y in range(y_max)))
