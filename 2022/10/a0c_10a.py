def signal_strength(cycle_nr, reg):
    return cycle_nr * reg


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

print(sum(signal_strength(i, register[i-1]) for i in range(20, 221, 40)))
