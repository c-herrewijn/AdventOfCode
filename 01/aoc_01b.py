with open("01/input.txt") as file1:
    lines = file1.readlines()
    subtotal = 0
    elves = []
    for line in lines:
        if (line == "\n"):
            elves.append((subtotal))
            subtotal = 0
        else:
            subtotal += int(line)

elves.sort(reverse=1)
total = elves[0] + elves[1] + elves[2]
print(total)