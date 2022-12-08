subtotal = 0
elves = []

with open("01/input.txt") as file:
    for line in file:
        if (line == "\n"):
            elves.append((subtotal))
            subtotal = 0
        else:
            subtotal += int(line)

elves.sort(reverse=1)
total = elves[0] + elves[1] + elves[2]
print(total)
