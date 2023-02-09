import re
import os
from functools import reduce

data = []

with open(os.getcwd() + '/day_07/input.txt') as file:
    for line in file:
        data.append(line.strip())

def create_dict(path, value):
    result_dict = value
    for key in reversed(path):
        result_dict = {key: result_dict}

    return result_dict


def get_nested_value(from_dict: dict, *keys):
    return reduce(lambda d, key: d.get(key) if d else None, keys, from_dict)


dir_sizes = {}
def count_dir_sizes(file_system, path):
    s = 0

    for k, v in file_system.items():
        if type(v) == int:
            s += v
        else:
            path.append(f"{k}/")
            s += count_dir_sizes(file_system[k], path)

    dir_sizes[''.join(path)] = s
    path.pop()
    return s


def filter_dir(dir_sizes, dir_size):
    return {k: v for (k, v) in dir_sizes.items() if v < dir_size and k != '/'}


def part_one(data):
    current_path = []
    file_system = {"/": {}}
    list_items = False

    for line in data:
        if line.startswith("$ cd"):
            folder = re.match("\$ cd (.*)", line)[1]
            list_items = False

            if folder == "..":
                current_path.pop()
            else:
                current_path.append(folder)

        elif line.startswith("$ ls"):
            list_items = True

        elif list_items:
            if line.startswith("dir"):
                folder = re.match("dir (.*)", line)[1]
                get_nested_value(file_system, *current_path).update({folder: {}})
            elif re.match("(\d*) (.*)", line):
                size, file_name = line.split(' ')
                get_nested_value(file_system, *current_path).update({file_name: int(size)})

        else:
            pass

    count_dir_sizes(file_system['/'], ['/'])
    count = sum(filter_dir(dir_sizes, 100_000).values())

    return count


def part_two(data):
    total_space = 70000000
    needed_space = 30000000
    free_space = total_space - dir_sizes['/']
    need_to_free = needed_space - free_space

    return min({k: v for (k, v) in dir_sizes.items() if v > need_to_free}.values())


print(part_one(data))
# print(part_two(data))

if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
