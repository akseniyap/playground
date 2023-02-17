from functools import reduce

from utils.py_utils.constants import INPUT
from utils.py_utils.decorators import strip_newlines, split_to_digits, to_list


@to_list
@split_to_digits
@strip_newlines
def get_data(variation):
    with open(f"inputs/08_{variation}.txt") as f:
        data = f.readlines()
    return data


def is_visible(current_tree, neighbours):
    return all(map(lambda tree: current_tree > tree, neighbours))


def view_distance(current_tree, trees):
    score = 0
    for tree in trees:
        score += 1
        if current_tree <= tree:
            return score

    return score


def easy(data):
    visible_trees = 0
    rows = len(data)
    cols = len(data[0])

    on_edge = lambda x, y: x == 0 or x == cols - 1 or y == 0 or y == rows - 1
    for j in range(rows):
        for i in range(cols):
            current_tree = data[j][i]

            if on_edge(i, j):
                visible_trees += 1
            else:
                left_trees = [data[j][x] for x in range(0, i)]
                right_trees = [data[j][x] for x in range(i + 1, cols)]
                up_trees = [data[y][i] for y in range(0, j)]
                down_trees = [data[y][i] for y in range(j + 1, rows)]

                if any([
                    is_visible(current_tree, left_trees),
                    is_visible(current_tree, right_trees),
                    is_visible(current_tree, up_trees),
                    is_visible(current_tree, down_trees)
                ]):
                    visible_trees += 1

    return visible_trees


def hard(data):
    rows = len(data)
    cols = len(data[0])
    view_distances = [[0 for _ in range(cols)] for _ in range(rows)]

    on_edge = lambda x, y: x == 0 or x == cols - 1 or y == 0 or y == rows - 1
    for j in range(rows):
        for i in range(cols):
            current_tree = data[j][i]

            if on_edge(i, j):
                view_distances[j][i] = 0
            else:
                left_trees = [data[j][x] for x in range(i - 1, -1, -1)]
                right_trees = [data[j][x] for x in range(i + 1, cols)]
                up_trees = [data[y][i] for y in range(j - 1, -1, -1)]
                down_trees = [data[y][i] for y in range(j + 1, rows)]

                scores = [
                    view_distance(current_tree, left_trees),
                    view_distance(current_tree, right_trees),
                    view_distance(current_tree, up_trees),
                    view_distance(current_tree, down_trees)
                ]
                view_distances[j][i] = reduce((lambda a, b: a * b), scores)

    distances = [item for sublist in view_distances for item in sublist]
    return max(distances)


if __name__ == "__main__":
    data = get_data(INPUT)
    print(easy(data))
    print(hard(data))
