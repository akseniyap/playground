import os
import re
from typing import Callable, List, Tuple

ROUNDS = 20
data = []
with open(os.getcwd() + "/AoC/2022/day_11/input.txt") as file:
    for line in file:
        data.append(line.strip())

monkey_data = [data[i:i+6] for i in range(0, len(data), 7)]


class Monkey:
    def __init__(self,
                name: int,
                items: List[int],
                expression: Tuple,
                test: Callable,
                test_arg: int,
                throw_if_true: int,
                throw_if_false: int):
        self.name = name
        self.items = items
        self.expression = expression
        self.test = test
        self.test_arg = test_arg
        self.throw_if_true = throw_if_true
        self.throw_if_false = throw_if_false
        self.inspections = 0


def foo(expression, worry_level):
    a, operator, b = expression
    a = worry_level
    if b == "old":
        b = worry_level
    else:
        b = int(b)

    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        return a / b

def bar(divisor, worry_level):
    return worry_level % divisor == 0


def create_monekys(monkey_data):
    monkeys = []
    for name, items, expression, test, true_op, false_op in monkey_data:
        name = int(re.match("Monkey (\\d*)", name)[1])

        items = re.match("Starting items: (.*)", items)[1]
        items = [int(item) for item in items.split(',')]

        matches = re.match("Operation: new = (old) (.*) (\\d+|old)", expression)
        expression = (matches[1], matches[2], matches[3])

        test_arg = int(re.match("Test: divisible by (\\d*)", test)[1])
        test = lambda x: x % test_arg == 0

        true_op = int(re.match("If true: throw to monkey (\\d*)", true_op)[1])
        false_op = int(re.match("If false: throw to monkey (\\d*)", false_op)[1])

        monkeys.append(Monkey(name, items, expression, test, test_arg, true_op, false_op))

    return monkeys


def part_one():
    monkeys = create_monekys(monkey_data)

    for _ in range(ROUNDS):
        for monkey in monkeys:
            for item in monkey.items:
                monkey.inspections += 1
                worry_level = item
                monkey.items = monkey.items[1:]
                worry_level = foo(monkey.expression, worry_level)
                worry_level //= 3

                # if monkey.test(worry_level):
                if bar(monkey.test_arg, worry_level):
                    monkeys[monkey.throw_if_true].items.append(worry_level)
                else:
                    monkeys[monkey.throw_if_false].items.append(worry_level)

    inspections = sorted([monkey.inspections for monkey in monkeys])
    a, b = inspections[-2:]
    return a * b


def part_two():
    monkeys = create_monekys(monkey_data)

    for _ in range(10_000):
        for monkey in monkeys:
            for item in monkey.items:
                monkey.inspections += 1
                worry_level = item
                monkey.items = monkey.items[1:]
                worry_level = foo(monkey.expression, worry_level)
                worry_level %= (13 * 19 * 11 * 17 * 3 * 7 * 5 * 2)
                # worry_level %= (23 * 19 * 13 * 17)
                # if monkey.test(worry_level):
                if bar(monkey.test_arg, worry_level):
                    monkeys[monkey.throw_if_true].items.append(worry_level)
                else:
                    monkeys[monkey.throw_if_false].items.append(worry_level)

    inspections = sorted([monkey.inspections for monkey in monkeys])
    a, b = inspections[-2:]
    return a * b


# print(part_one())
# print(part_two())

if __name__ == "__main__":
    # print(part_one())
    print(part_two())
    a = 1
