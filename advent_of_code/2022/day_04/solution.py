from utils.py_utils.constants import INPUT
from utils.py_utils.decorators import strip_newlines, split_lines_by, to_list


@to_list()
@split_lines_by(",")
@strip_newlines()
def get_data(variation):
    with open(f"inputs/04_{variation}.txt") as f:
        data = f.readlines()
    return data


containes = lambda a, b, c, d: (a <= c and b >= d) or (c <= a and d >= b)
overlaps = lambda a, b, c, d: (c <= a <= d) or (a <= c <= b)


def easy(data):
    count = 0
    for first_elf, second_elf in data:
        a, b = map(int, first_elf.split("-"))
        c, d = map(int, second_elf.split("-"))

        if containes(a, b, c, d):
            count += 1

    return count


def hard(data):
    count = 0
    for first_elf, second_elf in data:
        a, b = map(int, first_elf.split("-"))
        c, d = map(int, second_elf.split("-"))

        if overlaps(a, b, c, d):
            count += 1

    return count


if __name__ == "__main__":
    data = get_data(INPUT)
    print(easy(data))
    print(hard(data))
