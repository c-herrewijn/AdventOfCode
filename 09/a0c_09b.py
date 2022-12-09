def move_head(dir, h):
    dirs = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    return (h[0] + dirs[dir][0], h[1] + dirs[dir][1])


def move_knot(h, t):
    x_new = (int((h[0] + t[0]) / 2) if abs(h[0] - t[0]) == 2 else h[0])
    y_new = (int((h[1] + t[1]) / 2) if abs(h[1] - t[1]) == 2 else h[1])
    return (x_new, y_new)


knots = [(0, 0) for _ in range(10)]
trail = {(0, 0)}
with open("09/input.txt") as file:
    for line in file:
        dir, steps = line.strip().split()
        for _ in range(int(steps)):
            knots[0] = move_head(dir, knots[0])
            for i in range(1, 10):
                if abs(knots[i-1][0] - knots[i][0]) == 2 or abs(knots[i-1][1] - knots[i][1]) == 2:
                    knots[i] = move_knot(knots[i-1], knots[i])
            trail.add(knots[9])

print(len(trail))
