import re


data = []

with open('input.txt') as file:
    for line in file:
        data.append(line.strip())

# stacks = {1: ['Z', 'N'], 2: ['M', 'C', 'D'], 3: ['P']}
stacks = {
    1: ['H', 'C', 'R'],
    2: ['B', 'J', 'H', 'L', 'S', 'F'],
    3: ['R', 'M', 'D', 'H', 'J', 'T', 'Q'],
    4: ['S', 'G', 'R', 'H', 'Z', 'B', 'J'],
    5: ['R', 'P', 'F', 'Z', 'T', 'D', 'C', 'B'],
    6: ['T', 'H', 'C', 'G'],
    7: ['S', 'N', 'V', 'Z', 'B', 'P', 'W', 'L'],
    8: ['R', 'J', 'Q', 'G', 'C'],
    9: ['L', 'D', 'T', 'R', 'H', 'P', 'F', 'S']
}

def part_one(data):
    for line in data:
        matches = re.match("move (\d+) from (\d+) to (\d+)", line)
        count = int(matches[1])
        frm = int(matches[2])
        to = int(matches[3])

        for _ in range(count):
            crate = stacks[frm].pop()
            stacks[to].append(crate)

    # return ''.join([stacks[1][-1], stacks[2][-1], stacks[3][-1]])
    return ''.join([stacks[1][-1], stacks[2][-1], stacks[3][-1], stacks[4][-1], stacks[5][-1], stacks[6][-1], stacks[7][-1], stacks[8][-1], stacks[9][-1]])

print(part_one(data))


def part_two(data):
    for line in data:
        matches = re.match("move (\d+) from (\d+) to (\d+)", line)
        count = int(matches[1])
        frm = int(matches[2])
        to = int(matches[3])

        moving_crates = stacks[frm][len(stacks[frm])-count:]
        stacks[frm] = stacks[frm][:len(stacks[frm])-count]
        stacks[to] += moving_crates

    return ''.join([stacks[1][-1], stacks[2][-1], stacks[3][-1]])
    # return ''.join([stacks[1][-1], stacks[2][-1], stacks[3][-1], stacks[4][-1], stacks[5][-1], stacks[6][-1], stacks[7][-1], stacks[8][-1], stacks[9][-1]])


print(part_two(data))
