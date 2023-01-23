from utils.py_utils.constants import INPUT, NEW_LINE
from utils.py_utils.decorators import split_data, split_elements_by, to_ints


@to_ints()
@split_elements_by(NEW_LINE)
@split_data(2*NEW_LINE)
def get_data(variation):
    with open(f"inputs/01_{variation}.txt") as f:
        data = f.read()
    return data


def modify(data):
    return map(sum, data)


def easy(data):
    sums = modify(data)
    return max(sums)


def hard(data):
    sums = modify(data)
    return sum(sorted(sums)[-3:])


if __name__ == "__main__":
    data = list(get_data(INPUT))
    print(easy(data))
    print(hard(data))
