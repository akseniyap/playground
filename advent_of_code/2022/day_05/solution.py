import re

from utils.py_utils.constants import INPUT
from utils.py_utils.decorators import strip_newlines, to_list


@to_list
@strip_newlines
def get_data(variation):
    with open(f"inputs/05_{variation}.txt") as f:
        data = f.readlines()
    return data


def modify(data):
    def build_start_state(levels):
        levels = [crate.replace("    ", " [-] ") for crate in levels[:-1]]
        levels = [[crate[1] for crate in level.split()] for level in levels]
        stacks = [[] for _ in range(len(levels[-1])+1)]

        for level in reversed(levels):
            for index, crate in enumerate(level):
                if crate != "-":
                    stacks[index+1].append(crate)

        return stacks

    separator = data.index("")
    levels, instructions = data[:separator], data[separator+1:]
    stacks = build_start_state(levels)

    return stacks, instructions


def easy(data):
    stacks, instructions = modify(data)
    for instruction in instructions:
        matches = re.match("move (\d+) from (\d+) to (\d+)", instruction)
        qty, frm, to = map(int, matches.groups())

        for _ in range(qty):
            crate = stacks[frm].pop()
            stacks[to].append(crate)

    return "".join(map(lambda stack: stack[-1], stacks[1:]))


def hard(data):
    stacks, instructions = modify(data)
    for instruction in instructions:
        matches = re.match("move (\d+) from (\d+) to (\d+)", instruction)
        qty, frm, to = map(int, matches.groups())

        creates_to_move = stacks[frm][-qty:]
        stacks[frm] = stacks[frm][:-qty]
        stacks[to] += creates_to_move

    return "".join(map(lambda stack: stack[-1], stacks[1:]))


if __name__ == "__main__":
    data = get_data(INPUT)
    print(easy(data))
    print(hard(data))
