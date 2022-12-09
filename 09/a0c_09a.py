def move_head(dir, h):
    dirs = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    return (h[0] + dirs[dir][0], h[1] + dirs[dir][1])


def move_tail(h, t):
    x_new = (int((h[0] + t[0]) / 2) if abs(h[0] - t[0]) == 2 else h[0])
    y_new = (int((h[1] + t[1]) / 2) if abs(h[1] - t[1]) == 2 else h[1])
    return (x_new, y_new)


h = (0, 0)
t = (0, 0)
trail = {(0, 0)}
with open("09/input.txt") as file:
    for line in file:
        dir, steps = line.strip().split()
        for _ in range(int(steps)):
            h = move_head(dir, h)
            if abs(h[0] - t[0]) == 2 or abs(h[1] - t[1]) == 2:
                t = move_tail(h, t)
            trail.add(t)

print(len(trail))
