from utils.py_utils.constants import INPUT
from utils.py_utils.decorators import strip_newlines, split_lines_by, to_list


@to_list()
@split_lines_by(" ")
@strip_newlines()
def get_data(variation):
    with open(f"inputs/02_{variation}.txt") as f:
        data = f.readlines()
    return data


MOVE_SCORE = {"X": 1, "Y": 2, "Z": 3}
OUTCOME = {
    "AX": 3, "AY": 6, "AZ": 0,
    "BX": 0, "BY": 3, "BZ": 6,
    "CX": 6, "CY": 0, "CZ": 3
}
OPTION_FOR_OUTCOME = {
    "AX": "Z", "AY": "X", "AZ": "Y",
    "BX": "X", "BY": "Y", "BZ": "Z",
    "CX": "Y", "CY": "Z", "CZ": "X"
}


def easy(data):
    score = 0
    for his, my in data:
        score += OUTCOME[his + my]
        score += MOVE_SCORE[my]

    return score


def hard(data):
    score = 0
    for his, needed_outcome in data:
        my = OPTION_FOR_OUTCOME[his + needed_outcome]
        score += OUTCOME[his + my]
        score += MOVE_SCORE[my]

    return score


if __name__ == "__main__":
    data = get_data(INPUT)
    print(easy(data))
    print(hard(data))
