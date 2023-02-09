import os

data = []

with open(os.getcwd() + "/AoC/2022/day_09/input.txt") as file:
    for line in file:
        data.append([int(x) for x in line.strip()])

def part_one(data):
    return data


def part_two(data):
    return data


print(part_one(data))
print(part_two(data))

if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
