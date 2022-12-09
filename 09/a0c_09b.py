def move_head(dir, h):
    if (dir == 'U'):
        h[1] += 1
    if (dir == 'D'):
        h[1] -= 1
    if (dir == 'R'):
        h[0] += 1
    if (dir == 'L'):
        h[0] -= 1
    return h


def move_knot(h, t):
    if abs(h[0] - t[0]) == 2 or abs(h[1] - t[1]) == 2:
        if abs(h[0] - t[0]) == 2:
            t[0] = int((h[0] + t[0]) / 2)
        else:
            t[0] = h[0]
        if abs(h[1] - t[1]) == 2:
            t[1] = int((h[1] + t[1]) / 2)
        else:
            t[1] = h[1]
    return t


knots = [[0, 0] for _ in range(10)]
trail = {(0, 0)}
with open("09/input.txt") as file:
    for line in file:
        dir, steps = line.strip().split()
        for _ in range(int(steps)):
            knots[0] = move_head(dir, knots[0])
            for i in range(1, 10):
                knots[i] = move_knot(knots[i-1], knots[i])
            trail.add(tuple(knots[9]))

print(len(trail))
