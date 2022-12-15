import string

prio = 0
with open("03/input.txt") as file:

    for line in file:
        line = line.strip()
        len_half = int(len(line)/2)
        h1 = line[:len_half]
        h2 = line[len_half:]

        char = set(h1).intersection(h2).pop()
        if char.islower():
            prio += string.ascii_lowercase.find(char) + 1
        if char.isupper():
            prio += string.ascii_uppercase.find(char) + 27

print(prio)
