from utils.py_utils.constants import INPUT
from utils.py_utils.decorators import strip_newlines, to_ints, group_elements, sum_elements, to_list


@to_list()
@sum_elements()
@group_elements()
@to_ints()
@strip_newlines()
def get_data(variation):
    with open(f"inputs/01_{variation}.txt") as f:
        data = f.readlines()
    return data


def easy(data):
    return max(data)


def hard(data):
    return sum(sorted(data)[-3:])


if __name__ == "__main__":
    data = get_data(INPUT)
    print(easy(data))
    print(hard(data))
