def v_north(f, x, y):
    i = y - 1
    count = 0
    while i >= 0:
        count+=1
        if f[i][x] >= f[y][x]:
            break
        i-=1
    return count

def v_south(f, x, y, y_max):
    i = y + 1
    count = 0
    while i < y_max:
        count+=1
        if f[i][x] >= f[y][x]:
            break
        i+=1
    return count

def v_west(f, x, y):
    i = x - 1
    count = 0
    while i >= 0:
        count+=1
        if f[y][i] >= f[y][x]:
            break
        i-=1
    return count

def v_east(f, x, y, x_max):
    i = x + 1
    count = 0
    while i < x_max:
        count+=1
        if f[y][i] >= f[y][x]:
            break
        i+=1
    return count

def scenic_score(f, x, y, x_max, y_max):
    return v_north(f, x, y) * v_south(f, x, y, y_max) * v_west(f, x, y) * v_east(f, x, y, x_max)

f = []
with open("08/input.txt") as file:
    for y, line in enumerate(file):
        f.append([])
        for c in line.strip():
            f[y].append(int(c))

    y_max = len(f)
    x_max = len(f[0])
    print(max(scenic_score(f, x, y, x_max, y_max) for x in range(x_max) for y in range(y_max)))
