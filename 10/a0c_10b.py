register = [1]
cycle = 1

with open("10/input.txt") as file:
    for line in file:
        if line.strip() == "noop":
            register.append(register[cycle - 1])
            cycle += 1
        else:
            _, val = line.strip().split()
            register.append(register[cycle - 1])
            register.append(register[cycle - 1] + int(val))
            cycle += 2

s = ""
for i in range(0, len(register)):
    diff = (((i % 40)+1) - register[i])
    if diff == 2 or diff == 1 or diff == 0:
        s+="#"
    else:
        s+="."

print(s)
