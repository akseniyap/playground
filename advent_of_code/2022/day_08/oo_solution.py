from dataclasses import dataclass
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


@dataclass
class Tree:
    x: int
    y: int
    height: int


    def on_edge(self, rows, cols):
        return self.x == 0 or self.y == 0 or self.x == cols or self.y == rows


    def is_visible(self, neighbours):
        return all(map(lambda tree: self.height > tree.height, neighbours))


    def view_distance(self, trees):
        score = 0
        for tree in trees:
            score += 1
            if self.height <= tree.height:
                return score

        return score


class Board:
    def __init__(self):
        self.grid = []


    @property
    def rows(self):
        return len(self.grid)


    @property
    def cols(self):
        return len(self.grid[0])


    def get(self, x, y):
        return self.grid[y][x]


    def neighbours(self, tree):
        return [
            [self.grid[tree.y][x] for x in range(tree.x - 1, -1, -1)],    # left
            [self.grid[tree.y][x] for x in range(tree.x + 1, self.cols)], # right
            [self.grid[y][tree.x] for y in range(tree.y - 1, -1, -1)],    # up
            [self.grid[y][tree.x] for y in range(tree.y + 1, self.rows)]  # down
        ]


    @classmethod
    def parse_grid(cls, data):
        board = Board()
        board.grid = [
            [Tree(x, y, height) for x, height in enumerate(line)]
            for y, line
            in enumerate(data)
        ]
        return board


def easy(data):
    board = Board.parse_grid(data)
    visible_trees = 0

    for y in range(board.rows):
        for x in range(board.cols):
            tree = board.get(x, y)

            if tree.on_edge(board.rows, board.cols):
                visible_trees += 1
            else:
                neighbours = board.neighbours(tree)
                if any([tree.is_visible(trees) for trees in neighbours]):
                    visible_trees += 1

    return visible_trees


def hard(data):
    board = Board.parse_grid(data)
    view_distances = [[0 for _ in range(board.cols)] for _ in range(board.rows)]

    for y in range(board.rows):
        for x in range(board.cols):
            tree = board.get(x, y)

            if tree.on_edge(board.rows, board.cols):
                view_distances[y][x] = 0
            else:
                neighbours = board.neighbours(tree)
                scores = [tree.view_distance(trees) for trees in neighbours]
                view_distances[y][x] = reduce((lambda a, b: a * b), scores)

    flatten_scores = [item for sublist in view_distances for item in sublist]
    return max(flatten_scores)


if __name__ == "__main__":
    data = get_data(INPUT)
    print(easy(data))
    print(hard(data))
