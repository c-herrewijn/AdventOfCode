count = 0

with open("04/input.txt") as file:

    for line in file:
        e1, e2 = line.strip().split(",")
        e1_start, e1_end = list(map(int, e1.split("-")))
        e2_start, e2_end = list(map(int, e2.split("-")))

        # partial overlap:
        if (e1_start <= e2_end and e1_end >= e2_start):
            count += 1

print(count)
