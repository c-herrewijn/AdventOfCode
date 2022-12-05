import re

stacks = []
with open("05b/input.txt") as file1:
    lines = file1.readlines()
    for line in lines:

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
            stacks[to_stack] = stacks[from_stack][:nr_moves] + stacks[to_stack]
            stacks[from_stack] = stacks[from_stack][nr_moves:]

# result
print("".join(stacks[i][0] for i in range(nr_stacks)))
