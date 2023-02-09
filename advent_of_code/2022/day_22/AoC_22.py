import os
import re


data = []
with open(os.getcwd() + "/AoC/2022/day_22/sample.txt") as file:
    for line in file:
        data.append([*line.replace("\n", "")])

path = "".join(data.pop())
pairs = re.findall(r"([0-9]+)([A-Z]+)", '10R5L5R10L4R5L5')
rotations = {"L": "", "R": ""}

move_up = lambda x, y: (x, y+1)
move_down = lambda x, y: (x, y-1)
move_left = lambda x, y: (x-1, y)
move_right = lambda x, y: (x+1, y)

def part_one():
    pass


def part_two():
    pass

# print(part_one())
# print(part_two())


def main():
    a = 1
    # part_one()
    # part_two()


if __name__ == "__main__":
    main()
