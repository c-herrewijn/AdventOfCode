import re
import math


class Monkey:
    def __init__(self, start_items, operation, test_factor, next_mky_tf):
        self.start_items = start_items
        self.operation = operation
        self.test_factor = test_factor
        self.next_mky_tf = next_mky_tf
        self.number_inspections = 0
        self.mod_items = []

    def take_turn(self):
        while self.mod_items:
            self.inspect(self.mod_items[0])
            next_monkey = monkeys[self.next_mky_tf[0]] if self.test(self.mod_items[0]) else monkeys[self.next_mky_tf[1]]
            self.throw(next_monkey)
           
    def inspect(self, mod_item):
        self.number_inspections += 1
        if self.operation[0] == "+":
            mod_item.add_modulos(int(self.operation[1]))
        elif self.operation[0] == "*" and self.operation[1].isnumeric():
            mod_item.multiply_modulos(int(self.operation[1]))
        elif self.operation[0] == "*" and self.operation[1] == "old":
            mod_item.square_modulos()
        else:
            print("error")

    def test(self, mod_item):
        return(mod_item.modulos[divisors.index(self.test_factor)] == 0)

    def throw(self, next_monkey):
        next_monkey.mod_items.append(self.mod_items.pop(0))
  

class ModItem:
    def __init__(self, start_val, divisors):
        self.modulos = [start_val % divisor for divisor in divisors]

    def add_modulos(self, add_nr):
        self.modulos = [(mod + add_nr) % divisors[i] for i, mod in enumerate(self.modulos)]

    def multiply_modulos(self, factor):
        self.modulos = [(mod * factor) % divisors[i] for i, mod in enumerate(self.modulos)]

    def square_modulos(self):
        self.modulos = [(mod * mod) % divisors[i] for i, mod in enumerate(self.modulos)]


# parse data
monkeys = []
with open("11/input.txt") as file:
    lines = file.readlines()
    for m_line in range(1, len(lines), 7):
        start_items = list(map(int, re.match(r"^ *Starting items: (.*)", lines[m_line]).group(1).split(", ")))
        re_operation = re.match(r"^ +Operation: new = old (\+|\*) (.*)", lines[m_line+1])
        operation = (re_operation.group(1), re_operation.group(2))
        test_factor = int(re.match(r"^ *Test: divisible by ([0-9]+)", lines[m_line+2]).group(1))
        next_mky_true = int(re.match(r"^ *If true: throw to monkey ([0-9]+)", lines[m_line+3]).group(1))
        next_mky_false = int(re.match(r"^ *If false: throw to monkey ([0-9]+)", lines[m_line+4]).group(1))
        monkeys.append(Monkey(start_items, operation, test_factor, (next_mky_true, next_mky_false)))

# initialize divisors and mod objects
divisors = [m.test_factor for m in monkeys]
for m in monkeys:
    m.mod_items = [ModItem(start_val, divisors) for start_val in m.start_items]

# monkey business!
for _ in range(10000):
    for monkey in monkeys:
        monkey.take_turn()

# result
print(math.prod(sorted([monkey.number_inspections for monkey in monkeys], reverse=True)[0:2]))
