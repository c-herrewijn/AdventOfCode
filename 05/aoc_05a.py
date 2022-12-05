import re

stacks = []
with open("05/input.txt") as file:
    for line in file:

        # initial stacks
        if (stacks == []):
            nr_stacks = int(len(line)/4)
            stacks = [""]*nr_stacks
        if (re.match("^ *\[",line)):
            for i in range(nr_stacks):
                box = line[4*i + 1]
                if box != " ":
                    stacks[i] += box

        # process instructions
        instructions = re.match(r"^move (\d+) from (\d+) to (\d+)",line)
        if (instructions):
            nr_moves = int(instructions.group(1))
            from_stack = int(instructions.group(2)) - 1
            to_stack = int(instructions.group(3)) - 1 
            for i in range(nr_moves):
                stacks[to_stack] = stacks[from_stack][0] + stacks[to_stack]
                stacks[from_stack] = stacks[from_stack][1:]

# result
print("".join(stacks[i][0] for i in range(nr_stacks)))
