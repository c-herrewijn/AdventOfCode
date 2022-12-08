def v_north(f, x, y):
    y_coord_block = next((i for i in range(y-1, 0, -1) if (f[i][x] >= f[y][x])), 0)
    return(y - y_coord_block)

def v_south(f, x, y, y_max):
    y_coord_block = next((i for i in range(y+1, y_max) if (f[i][x] >= f[y][x])), y_max - 1)
    return(y_coord_block - y)

def v_west(f, x, y):
    x_coord_block = next((i for i in range(x-1, 0, -1) if (f[y][i] >= f[y][x])), 0)
    return(x - x_coord_block)

def v_east(f, x, y, x_max):
    x_coord_block = next((i for i in range(x+1, x_max) if (f[y][i] >= f[y][x])), x_max - 1)
    return(x_coord_block - x)

def scenic_score(f, x, y, x_max, y_max):
    return v_north(f, x, y) * v_south(f, x, y, y_max) * v_west(f, x, y) * v_east(f, x, y, x_max)

with open("08/input.txt") as file:
    f = [[char for char in line.strip()] for line in file]
    y_max = len(f)
    x_max = len(f[0])
    print(max(scenic_score(f, x, y, x_max, y_max) for x in range(x_max) for y in range(y_max)))
