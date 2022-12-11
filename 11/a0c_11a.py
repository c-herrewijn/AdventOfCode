import re
import math


class Monkey:
    def __init__(self, items, operation, test_factor, next_mky_tf):
        self.items = items
        self.operation = operation
        self.test_factor = test_factor
        self.next_mky_tf = next_mky_tf
        self.number_inspections = 0


monkeys = []
with open("11/input.txt") as file:
    lines = file.readlines()
    for m_line in range(1, len(lines), 7):
        items = list(map(int, re.match(r"^ *Starting items: (.*)", lines[m_line]).group(1).split(", ")))
        re_operation = re.match(r"^ +Operation: new = old (\+|\*) (.*)", lines[m_line+1])
        operation = (re_operation.group(1), re_operation.group(2))
        test_factor = int(re.match(r"^ *Test: divisible by ([0-9]+)", lines[m_line+2]).group(1))
        next_mky_true = int(re.match(r"^ *If true: throw to monkey ([0-9]+)", lines[m_line+3]).group(1))
        next_mky_false = int(re.match(r"^ *If false: throw to monkey ([0-9]+)", lines[m_line+4]).group(1))
        monkeys.append(Monkey(items, operation, test_factor, (next_mky_true, next_mky_false)))

for r in range(20):
    for monkey in monkeys:
        while monkey.items:
            monkey.number_inspections += 1
            item = monkey.items.pop(0)
            operand = item if monkey.operation[1] == "old" else int(monkey.operation[1])
            item = int((item * operand) / 3) if monkey.operation[0] == "*" else int((item + operand) / 3)
            monkeys[monkey.next_mky_tf[0]].items.append(item) if item % monkey.test_factor == 0 else monkeys[monkey.next_mky_tf[1]].items.append(item)

print(math.prod(sorted([monkey.number_inspections for monkey in monkeys], reverse=True)[0:2]))
