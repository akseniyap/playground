import os
from functools import reduce

data = []

with open(os.getcwd() + '/day_08/input.txt') as file:
    for line in file:
        data.append([int(x) for x in line.strip()])


def is_visible(current_tree, trees):
    return all(map(lambda x: x < current_tree, trees))


def scenic_score(current_tree, trees):
    score = 0

    for tree in trees:
        if current_tree > tree:
            score += 1
        elif current_tree <= tree:
            score += 1
            return score
        else:
            return score

    return score



def part_one(data):
    visible_trees = 0
    rows = len(data)
    cols = len(data[0])

    for i in range(cols):
        for j in range(rows):
            current_tree = data[j][i]

            if j == 0 or j == (rows - 1) or i == 0 or i == (cols - 1):
                visible_trees += 1
            else:
                left_trees = [data[j][x] for x in range(0, i)]
                right_trees = [data[j][x] for x in range(i + 1, cols)]
                top_trees = [data[y][i] for y in range(0, j)]
                bottom_trees = [data[y][i] for y in range(j + 1, rows)]

                if any([
                    is_visible(current_tree, left_trees),
                    is_visible(current_tree, right_trees),
                    is_visible(current_tree, top_trees),
                    is_visible(current_tree, bottom_trees)
                ]):
                    visible_trees += 1

    return visible_trees


def part_two(data):
    rows = len(data)
    cols = len(data[0])
    scenic_scores = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            current_tree = data[i][j]

            if i == 0 or i == (rows - 1) or j == 0 or j == (cols - 1):
                scenic_scores[i][j] = 0
            else:
                left_trees = [data[i][x] for x in range(j - 1, -1, -1)]
                right_trees = [data[i][x] for x in range(j + 1, cols)]
                top_trees = [data[y][j] for y in range(i - 1, -1, -1)]
                bottom_trees = [data[y][j] for y in range(i + 1, rows)]

                scores = [
                    scenic_score(current_tree, left_trees),
                    scenic_score(current_tree, right_trees),
                    scenic_score(current_tree, top_trees),
                    scenic_score(current_tree, bottom_trees)
                ]
                score = reduce((lambda x, y: x * y), scores)
                scenic_scores[i][j] = score

    scores = [item for sublist in scenic_scores for item in sublist]
    return max(scores)


print(part_one(data))
print(part_two(data))

if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
