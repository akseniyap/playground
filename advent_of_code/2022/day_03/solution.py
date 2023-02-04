from string import ascii_letters
from utils.py_utils.constants import INPUT, NEW_LINE
from utils.py_utils.decorators import split_data


@split_data(NEW_LINE)
def get_data(variation):
    with open(f"inputs/03_{variation}.txt") as f:
        data = f.read()
    return data


LETTERS = list(ascii_letters)

common_item = lambda el: set.intersection(*(map(set, el))).pop()
priority = lambda el: LETTERS.index(el) + 1


def easy(data):
    compartments = [[el[:len(el)//2], el[len(el)//2:]] for el in data]
    common_items = [common_item(el) for el in compartments]
    priorities = [priority(el) for el in common_items]

    return sum(priorities)


def hard(data):
    groups = [data[i:i+3] for i in range(0, len(data), 3)]
    common_items = [common_item(el) for el in groups]
    priorities = [priority(el) for el in common_items]

    return sum(priorities)


if __name__ == "__main__":
    data = list(get_data(INPUT))
    print(easy(data))
    print(hard(data))
