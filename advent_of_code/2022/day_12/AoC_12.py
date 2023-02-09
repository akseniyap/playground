import os

data = []
with open(os.getcwd() + "/AoC/2022/day_12/sample.txt") as file:
    for line in file:
        data.append([char for char in line.strip()])


def part_one():
    return data


def part_two():
    return data


print(part_one())
# print(part_two())

if __name__ == "__main__":
    pass
    # print(part_one())
    # print(part_two())
