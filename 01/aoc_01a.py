subtotal = 0
max = 0

with open("01/input.txt") as file:
    for line in file:
        if (line == "\n"):
            subtotal = 0
        else:
            subtotal += int(line)
            if subtotal > max:
                max = subtotal

print(max)
