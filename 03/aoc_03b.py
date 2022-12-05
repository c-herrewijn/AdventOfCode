import string

prio = 0
with open("03/input.txt") as file:
    lines = file.readlines()

    for group in range(int(len(lines) / 3)):
        elf1 = lines[3 * group].strip()
        elf2 = lines[3 * group + 1].strip()
        elf3 = lines[3 * group + 2].strip()

        char = set(elf1).intersection(elf2).intersection(elf3).pop()
        if char.islower():
            prio += string.ascii_lowercase.find(char) + 1
        if char.isupper():
            prio += string.ascii_uppercase.find(char) + 27

print(prio)
