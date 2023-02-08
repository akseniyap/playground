from elf import Elf
from utils.py_utils.constants import INPUT
from utils.py_utils.decorators import strip_newlines, split_lines_by, to_list


@to_list
@split_lines_by("[,-]")
@strip_newlines
def get_data(variation):
    with open(f"inputs/04_{variation}.txt") as f:
        data = f.readlines()
    return data


def modify(data):
    elves = []
    for first_start, first_end, second_start, second_end in data:
        first_elf = Elf(int(first_start), int(first_end))
        second_elf = Elf(int(second_start), int(second_end))
        elves.append([first_elf, second_elf])

    return elves


def easy(data):
    count = 0
    elves = modify(data)
    for first_elf, second_elf in elves:
        if first_elf.contains(second_elf) or second_elf.contains(first_elf):
            count += 1

    return count


def hard(data):
    count = 0
    elves = modify(data)
    for first_elf, second_elf in elves:
        if first_elf.overlaps(second_elf) or second_elf.overlaps(first_elf):
            count += 1

    return count


if __name__ == "__main__":
    data = get_data(INPUT)
    print(easy(data))
    print(hard(data))
