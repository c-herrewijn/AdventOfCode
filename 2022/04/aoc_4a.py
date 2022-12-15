count = 0

with open("04/input.txt") as file:

    for line in file:
        e1, e2 = line.strip().split(",")
        e1_start, e1_end = list(map(int, e1.split("-")))
        e2_start, e2_end = list(map(int, e2.split("-")))

        # full overlap:
        if (e1_start <= e2_start and e1_end >= e2_end) or (e2_start <= e1_start and e2_end >= e1_end):
            count += 1

print(count)
