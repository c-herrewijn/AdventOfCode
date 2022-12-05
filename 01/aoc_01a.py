with open("01/input.txt") as file1:
    lines = file1.readlines()
    max = 0
    subtotal = 0
    for line in lines:
        if (line == "\n"):
            subtotal = 0
        else:
            subtotal += int(line)
            if subtotal > max:
                max = subtotal

print(max)
