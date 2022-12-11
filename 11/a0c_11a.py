import re
import math


class Monkey:
    def __init__(self, items, operation, test_factor, next_mky_tf):
        self.items = items
        self.operation = operation
        self.test_factor = test_factor
        self.next_mky_tf = next_mky_tf
        self.number_inspections = 0

    def take_turn(self):
        while self.items:
            self.items[0] = self.inspect(self.items[0])
            next_monkey = monkeys[self.next_mky_tf[0]] if self.test(self.items[0]) else monkeys[self.next_mky_tf[1]]
            self.throw(next_monkey)
           
    def inspect(self, item):
        self.number_inspections += 1
        operand = item if self.operation[1] == "old" else int(self.operation[1])
        return int((item * operand) / 3) if self.operation[0] == "*" else int((item + operand) / 3)

    def test(self, item):
        return item % self.test_factor == 0

    def throw(self, next_monkey):
        next_monkey.items.append(self.items.pop(0))
  

# parse data
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

# monkey business!
for _ in range(20):
    for monkey in monkeys:
        monkey.take_turn()

# result
print(math.prod(sorted([monkey.number_inspections for monkey in monkeys], reverse=True)[0:2]))
