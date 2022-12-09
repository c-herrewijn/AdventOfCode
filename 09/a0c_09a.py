def move_head(dir, h):
    dirs = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    h = [h[i] + dirs[dir][i] for i in range(2)]
    return h


def move_tail(h, t):
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


h = [0, 0]
t = [0, 0]
trail = {(0, 0)}
with open("09/input.txt") as file:
    for line in file:
        dir, steps = line.strip().split()
        for _ in range(int(steps)):
            h = move_head(dir, h)
            t = move_tail(h, t)
            trail.add(tuple(t))

print(len(trail))
